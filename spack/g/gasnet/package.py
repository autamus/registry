# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack import *


class Gasnet(Package):
    """GASNet is a language-independent, networking middleware layer that
       provides network-independent, high-performance communication primitives
       including Remote Memory Access (RMA) and Active Messages (AM). It has been
       used to implement parallel programming models and libraries such as UPC,
       UPC++, Co-Array Fortran, Legion, Chapel, and many others. The interface is
       primarily intended as a compilation target and for use by runtime library
       writers (as opposed to end users), and the primary goals are high
       performance, interface portability, and expressiveness.

       ***NOTICE***: The GASNet library built by this Spack package is ONLY intended for
       unit-testing purposes, and is generally UNSUITABLE FOR PRODUCTION USE.
       The RECOMMENDED way to build GASNet is as an embedded library as configured
       by the higher-level client runtime package (UPC++, Legion, etc), including
       system-specific configuration.
    """
    homepage = "https://gasnet.lbl.gov"
    url      = "https://gasnet.lbl.gov/EX/GASNet-2021.3.0.tar.gz"
    git      = "https://bitbucket.org/berkeleylab/gasnet.git"

    maintainers = ['PHHargrove', 'bonachea']

    tags = ['e4s']

    version('develop', branch='develop')
    version('main',    branch='stable')
    version('master',  branch='master')

    version('2021.9.0',  sha256='1b6ff6cdad5ecf76b92032ef9507e8a0876c9fc3ee0ab008de847c1fad0359ee')
    version('2021.3.0',  sha256='8a40fb3fa8bacc3922cd4d45217816fcb60100357ab97fb622a245567ea31747')
    version('2020.10.0', sha256='ed17baf7fce90499b539857ee37b3eea961aa475cffbde77e4c607a34ece06a0')
    version('2020.3.0',  sha256='019eb2d2284856e6fabe6c8c0061c874f10e95fa0265245f227fd3497f1bb274')
    version('2019.9.0',  sha256='117f5fdb16e53d0fa8a47a1e28cccab1d8020ed4f6e50163d985dc90226aaa2c')
    # Do NOT add older versions here.
    # GASNet-EX releases over 2 years old are not supported.

    # The optional network backends:
    variant('conduits',
            values=any_combination_of('smp', 'mpi', 'ibv', 'udp').with_default('smp'),
            description="The hardware-dependent network backends to enable.\n" +
                        "(smp) = SMP conduit for single-node operation ;\n" +
                        "(ibv) = Native InfiniBand verbs conduit ;\n" +
                        "(udp) = Portable UDP conduit, for Ethernet networks ;\n" +
                        "(mpi) = Low-performance/portable MPI conduit ;\n" +
                        "For detailed recommendations, consult https://gasnet.lbl.gov")

    variant('debug', default=False, description="Enable library debugging mode")

    depends_on('mpi', when='conduits=mpi')

    depends_on('autoconf@2.69', type='build', when='@master:')
    depends_on('automake@1.16:', type='build', when='@master:')

    def install(self, spec, prefix):
        if spec.satisfies('@master:'):
            bootstrapsh = Executable("./Bootstrap")
            bootstrapsh()

        # The GASNet-EX library has a highly multi-dimensional configure space,
        # to accomodate the varying behavioral requirements of each client runtime.
        # The library's ABI/link compatibility is strongly dependent on these
        # client-specific build-time settings, and that variability is deliberately NOT
        # encoded in the variants of this package. The recommended way to build/deploy
        # GASNet is as an EMBEDDED library within the build of the client package
        # (eg. Berkeley UPC, UPC++, Legion, etc), some of which provide build-time
        # selection of the GASNet library sources. This spack package provides
        # the GASNet-EX sources, for use by appropriate client packages.
        install_tree('.', prefix + "/src")

        # Library build is provided for unit-testing purposes only (see notice above)
        if 'conduits=none' not in spec:
            options = ["--prefix=%s" % prefix]

            if '+debug' in spec:
                options.append("--enable-debug")

            if 'conduits=mpi' in spec:
                options.append("--enable-mpi-compat")
            else:
                options.append("--disable-mpi-compat")

            options.append("--disable-auto-conduit-detect")
            for c in spec.variants['conduits'].value:
                options.append("--enable-" + c)

            configure(*options)
            make()
            make('install')

            for c in spec.variants['conduits'].value:
                testdir = join_path(self.prefix.tests, c)
                mkdirp(testdir)
                make('-C', c + '-conduit', 'testgasnet-par')
                install(c + "-conduit/testgasnet", testdir)
            make('-C', c + '-conduit', 'testtools-par')
            install(c + "-conduit/testtools", self.prefix.tests)

    @run_after('install')
    @on_package_attributes(run_tests=True)
    def test_install(self):
        if 'conduits=smp' in self.spec:
            make('-C', 'smp-conduit', 'run-tests')
        if 'conduits=none' not in self.spec:
            self.run_test(join_path(self.prefix.tests, 'testtools'),
                          expected=['Done.'], status=0,
                          installed=True, purpose="Running testtools")

    def test(self):
        if 'conduits=none' in self.spec:
            spack.main.send_warning_to_tty("No conduit libraries built -- SKIPPED")
            return

        ranks = '4'
        spawner = {
            'smp': ['env', 'GASNET_PSHM_NODES=' + ranks],
            'mpi': [join_path(self.prefix.bin, 'gasnetrun_mpi'), '-n', ranks],
            'ibv': [join_path(self.prefix.bin, 'gasnetrun_ibv'), '-n', ranks],
            'udp': [join_path(self.prefix.bin, 'amudprun'), '-spawn', 'L', '-np', ranks]
        }

        os.environ['GASNET_VERBOSEENV'] = '1'  # include diagnostic info
        if 'GASNET_SSH_SERVERS' not in os.environ:
            os.environ['GASNET_SSH_SERVERS'] = "localhost " * 4

        self.run_test(join_path(self.prefix.tests, 'testtools'),
                      expected=['Done.'], status=0,
                      installed=True, purpose="Running testtools")

        for c in self.spec.variants['conduits'].value:
            os.environ['GASNET_SUPERNODE_MAXSIZE'] = '0' if (c == 'smp') else '1'
            test = join_path(self.prefix.tests, c, 'testgasnet')
            self.run_test(spawner[c][0], spawner[c][1:] + [test],
                          expected=['done.'], status=0,
                          installed=(c != 'smp'),
                          purpose="Running %s-conduit/testgasnet" % c)

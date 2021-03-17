# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os
import sys


class Hypre(Package, CudaPackage):
    """Hypre is a library of high performance preconditioners that
       features parallel multigrid methods for both structured and
       unstructured grid problems."""

    homepage = "http://computing.llnl.gov/project/linear_solvers/software.php"
    url      = "https://github.com/hypre-space/hypre/archive/v2.20.0.tar.gz"
    git      = "https://github.com/hypre-space/hypre.git"

    maintainers = ['ulrikeyang', 'osborn9', 'balay']

    test_requires_compiler = True
    version('2.20.0', sha256='5be77b28ddf945c92cde4b52a272d16fb5e9a7dc05e714fc5765948cba802c01', url='https://github.com/hypre-space/hypre/archive/v2.20.0.tar.gz')

    # Versions 2.13.0 and later can be patched to build shared
    # libraries on Darwin; the patch for this capability does not
    # apply to version 2.12.1 and earlier due to changes in the build system
    # between versions 2.12.1 and 2.13.0.
    variant('shared', default=(sys.platform != 'darwin'),
            description="Build shared library (disables static library)")
    # Use internal SuperLU routines for FEI - version 2.12.1 and below
    variant('internal-superlu', default=False,
            description="Use internal SuperLU routines")
    variant('superlu-dist', default=False,
            description='Activates support for SuperLU_Dist library')
    variant('int64', default=False,
            description="Use 64bit integers")
    variant('mixedint', default=False,
            description="Use 64bit integers while reducing memory use")
    variant('complex', default=False, description='Use complex values')
    variant('mpi', default=True, description='Enable MPI support')
    variant('openmp', default=False, description='Enable OpenMP support')
    variant('debug', default=False,
            description='Build debug instead of optimized version')

    # Patch to add ppc64le in config.guess
    patch('ibm-ppc64le.patch', when='@:2.11.1')

    # Patch to build shared libraries on Darwin
    patch('darwin-shared-libs-for-hypre-2.13.0.patch', when='+shared@2.13.0 platform=darwin')
    patch('darwin-shared-libs-for-hypre-2.14.0.patch', when='+shared@2.14.0 platform=darwin')
    patch('superlu-dist-link-2.15.0.patch', when='+superlu-dist @2.15:2.16.0')
    patch('superlu-dist-link-2.14.0.patch', when='+superlu-dist @:2.14.0')
    patch('hypre21800-compat.patch', when='@2.18.0')
    # Patch to get config flags right
    patch('detect-compiler.patch', when='@2.15.0:2.20.0')

    depends_on("mpi", when='+mpi')
    depends_on("blas")
    depends_on("lapack")
    depends_on('superlu-dist', when='+superlu-dist+mpi')

    conflicts('+cuda', when='+int64')

    # Patch to build shared libraries on Darwin does not apply to
    # versions before 2.13.0
    conflicts("+shared@:2.12.99 platform=darwin")

    # Conflicts
    # Option added in v2.13.0
    conflicts('+superlu-dist', when='@:2.12.99')

    # Internal SuperLU Option removed in v2.13.0
    conflicts('+internal-superlu', when='@2.13.0:')

    # Option added in v2.16.0
    conflicts('+mixedint', when='@:2.15.99')

    def url_for_version(self, version):
        if version >= Version('2.12.0'):
            url = 'https://github.com/hypre-space/hypre/archive/v{0}.tar.gz'
        else:
            url = 'http://computing.llnl.gov/project/linear_solvers/download/hypre-{0}.tar.gz'

        return url.format(version)

    def _configure_args(self):
        spec = self.spec
        # Note: --with-(lapack|blas)_libs= needs space separated list of names
        lapack = spec['lapack'].libs
        blas = spec['blas'].libs

        configure_args = [
            '--prefix=%s' % prefix,
            '--with-lapack-libs=%s' % ' '.join(lapack.names),
            '--with-lapack-lib-dirs=%s' % ' '.join(lapack.directories),
            '--with-blas-libs=%s' % ' '.join(blas.names),
            '--with-blas-lib-dirs=%s' % ' '.join(blas.directories)
        ]

        if '+mpi' in self.spec:
            os.environ['CC'] = spec['mpi'].mpicc
            os.environ['CXX'] = spec['mpi'].mpicxx
            os.environ['F77'] = spec['mpi'].mpif77
            configure_args.append('--with-MPI')
        else:
            configure_args.append('--without-MPI')

        if '+openmp' in self.spec:
            configure_args.append('--with-openmp')
        else:
            configure_args.append('--without-openmp')

        if '+int64' in self.spec:
            configure_args.append('--enable-bigint')
        else:
            configure_args.append('--disable-bigint')

        if '+mixedint' in self.spec:
            configure_args.append('--enable-mixedint')
        else:
            configure_args.append('--disable-mixedint')

        if '+complex' in self.spec:
            configure_args.append('--enable-complex')
        else:
            configure_args.append('--disable-complex')

        if '+shared' in self.spec:
            configure_args.append("--enable-shared")

        if '~internal-superlu' in self.spec:
            configure_args.append("--without-superlu")
            # MLI and FEI do not build without superlu on Linux
            configure_args.append("--without-mli")
            configure_args.append("--without-fei")

        if '+superlu-dist' in self.spec:
            configure_args.append('--with-dsuperlu-include=%s' %
                                  spec['superlu-dist'].prefix.include)
            configure_args.append('--with-dsuperlu-lib=%s' %
                                  spec['superlu-dist'].libs)
            configure_args.append('--with-dsuperlu')

        if '+debug' in self.spec:
            configure_args.append("--enable-debug")
        else:
            configure_args.append("--disable-debug")

        if '+cuda' in self.spec:
            configure_args.extend([
                '--with-cuda',
                '--enable-curand',
                '--enable-cub'
            ])
        else:
            configure_args.extend([
                '--without-cuda',
                '--disable-curand',
                '--disable-cub'
            ])

        return configure_args

    def setup_build_environment(self, env):
        if '+mpi' in self.spec:
            env.set('CC', self.spec['mpi'].mpicc)
            env.set('CXX', self.spec['mpi'].mpicxx)
            env.set('F77', self.spec['mpi'].mpif77)

        if '+cuda' in self.spec:
            env.set('CUDA_HOME', self.spec['cuda'].prefix)
            env.set('CUDA_PATH', self.spec['cuda'].prefix)
            cuda_arch = self.spec.variants['cuda_arch'].value
            if cuda_arch:
                arch_sorted = list(sorted(cuda_arch, reverse=True))
                env.set('HYPRE_CUDA_SM', arch_sorted[0])
            # In CUDA builds hypre currently doesn't handle flags correctly
            env.append_flags(
                'CXXFLAGS', '-O2' if '~debug' in self.spec else '-g')

    def install(self, spec, prefix):
        configure_args = self._configure_args()
        # Hypre's source is staged under ./src so we'll have to manually
        # cd into it.
        with working_dir("src"):
            configure(*configure_args)

            make()
            if self.run_tests:
                make("check")
                make("test")
                Executable(join_path('test', 'ij'))()
                sstruct = Executable(join_path('test', 'struct'))
                sstruct()
                sstruct('-in', 'test/sstruct.in.default', '-solver', '40',
                        '-rhsone')
            make("install")

    @run_after('install')
    def cache_test_sources(self):
        srcs = ['src/examples']
        self.cache_extra_test_sources(srcs)

    def test(self):
        """Perform smoke test on installed HYPRE package."""

        if '+mpi' in self.spec:
            examples_dir = join_path(self.install_test_root, 'src/examples')
            with working_dir(examples_dir, create=False):
                make("HYPRE_DIR=" + self.prefix, "bigint")

                reason = "test: ensuring HYPRE examples run"
                self.run_test('./ex5big', [], [], installed=True,
                              purpose=reason, skip_missing=True, work_dir='.')
                self.run_test('./ex15big', [], [], installed=True,
                              purpose=reason, skip_missing=True, work_dir='.')

                make("distclean")

    @property
    def headers(self):
        """Export the main hypre header, HYPRE.h; all other headers can be found
        in the same directory.
        Sample usage: spec['hypre'].headers.cpp_flags
        """
        hdrs = find_headers('HYPRE', self.prefix.include, recursive=False)
        return hdrs or None

    @property
    def libs(self):
        """Export the hypre library.
        Sample usage: spec['hypre'].libs.ld_flags
        """
        is_shared = '+shared' in self.spec
        libs = find_libraries('libHYPRE', root=self.prefix, shared=is_shared,
                              recursive=True)
        return libs or None


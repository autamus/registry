# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pumi(CMakePackage):
    """SCOREC RPI's Parallel Unstructured Mesh Infrastructure (PUMI).
       An efficient distributed mesh data structure and methods to support
       parallel adaptive analysis including general mesh-based operations,
       such as mesh entity creation/deletion, adjacency and geometric
       classification, iterators, arbitrary (field) data attachable to mesh
       entities, efficient communication involving entities duplicated
       across multiple tasks, migration of mesh entities between tasks,
       and dynamic load balancing."""

    homepage = "https://www.scorec.rpi.edu/pumi"
    git      = "https://github.com/SCOREC/core.git"

    maintainers = ['cwsmith']

    # We will use the scorec/core master branch as the 'nightly' version
    # of pumi in spack.  The master branch is more stable than the
    # scorec/core develop branch and we perfer not to expose spack users
    # to the added instability.    url      = ""

    version('master', branch='master', submodules=True, expand=False)
    version('2.2.6', expand=False)
    version('2.2.5', expand=False)
    version('2.2.4', expand=False)
    version('2.2.3', expand=False)
    version('2.2.2', expand=False)
    version('2.2.1', expand=False)
    version('2.2.0', expand=False)
    version('2.1.0', expand=False)

    variant('int64', default=False, description='Enable 64bit mesh entity ids')
    variant('shared', default=False, description='Build shared libraries')
    variant('zoltan', default=False, description='Enable Zoltan Features')
    variant('fortran', default=False, description='Enable FORTRAN interface')
    variant('testing', default=False, description='Enable tests')
    variant('simmodsuite', default='none',
            values=('none', 'base', 'kernels', 'full'),
            description="Enable Simmetrix SimModSuite Support: 'base' enables "
            "the minimum set of functionality, 'kernels' adds CAD kernel "
            "support to 'base', and 'full' enables all functionality.")
    variant('simmodsuite_version_check', default=True,
            description="Enable check of Simmetrix SimModSuite version. "
            "Disable the check for testing new versions.")

    depends_on('mpi')
    depends_on('cmake@3:', type='build')
    depends_on('zoltan', when='+zoltan')
    depends_on('zoltan+int64', when='+zoltan+int64')
    simbase = "+base"
    simkernels = simbase + "+parasolid+acis+discrete"
    simfull = simkernels + "+abstract+adv+advmodel\
                            +import+paralleladapt+parallelmesh"
    depends_on('simmetrix-simmodsuite' + simbase,
               when='simmodsuite=base')
    depends_on('simmetrix-simmodsuite' + simkernels,
               when='simmodsuite=kernels')
    depends_on('simmetrix-simmodsuite' + simfull,
               when='simmodsuite=full')

    def cmake_args(self):
        spec = self.spec

        args = [
            '-DSCOREC_CXX_WARNINGS=OFF',
            self.define_from_variant('ENABLE_ZOLTAN', 'zoltan'),
            '-DCMAKE_C_COMPILER=%s' % spec['mpi'].mpicc,
            '-DCMAKE_CXX_COMPILER=%s' % spec['mpi'].mpicxx,
            self.define_from_variant('BUILD_SHARED_LIBS', 'shared'),
            '-DCMAKE_Fortran_COMPILER=%s' % spec['mpi'].mpifc,
            self.define_from_variant('PUMI_FORTRAN_INTERFACE', 'fortran'),
            '-DMDS_ID_TYPE=%s' % ('long' if '+int64' in spec else 'int'),
            '-DSKIP_SIMMETRIX_VERSION_CHECK=%s' %
            ('ON' if '~simmodsuite_version_check' in spec else 'OFF'),
            self.define_from_variant('IS_TESTING', 'testing'),
            '-DMESHES=%s' % join_path(self.stage.source_path, 'pumi-meshes')
        ]
        if spec.satisfies('@2.2.3'):
            args += ['-DCMAKE_CXX_STANDARD=11']
        if self.spec.satisfies('simmodsuite=base'):
            args.append('-DENABLE_SIMMETRIX=ON')
        if self.spec.satisfies('simmodsuite=kernels') or \
           self.spec.satisfies('simmodsuite=full'):
            args.append('-DENABLE_SIMMETRIX=ON')
            args.append('-DSIM_PARASOLID=ON')
            args.append('-DSIM_ACIS=ON')
            args.append('-DSIM_DISCRETE=ON')
            mpi_id = spec['mpi'].name + spec['mpi'].version.string
            args.append('-DSIM_MPI=' + mpi_id)
        return args

    @run_after('build')
    @on_package_attributes(run_tests=True)
    def check(self):
        """Run ctest after building project."""

        with working_dir(self.build_directory):
            ctest(parallel=False)

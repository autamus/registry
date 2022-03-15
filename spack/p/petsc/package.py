# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os


class Petsc(Package, CudaPackage, ROCmPackage):
    """PETSc is a suite of data structures and routines for the scalable
    (parallel) solution of scientific applications modeled by partial
    differential equations.
    """

    homepage = "https://www.mcs.anl.gov/petsc/index.html"
    url      = "https://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.15.0.tar.gz"
    git = "https://gitlab.com/petsc/petsc.git"
    maintainers = ['balay', 'barrysmith', 'jedbrown']

    tags = ['e4s']

    version('main', branch='main')
    version('3.16.5', sha256='7de8570eeb94062752d82a83208fc2bafc77b3f515023a4c14d8ff9440e66cac')
    version('3.16.4', sha256='229cce22bdcfedb1fe827d306ed1afca9737786cdc3f0562b74a1966c1243caf')
    version('3.16.3', sha256='eff44c7e7f12991dc7d2b627c477807a215ce16c2ce8a1c78aa8237ddacf6ca5')
    version('3.16.2', sha256='7ab257ae150d4837ac8d3872a1d206997962578785ec2427639ceac46d131bbc')
    version('3.16.1', sha256='909cf7bce7b6a0ddb2580a1ac9502aa01631ec4105c716594c1804f0ee1ea06a')
    version('3.16.0', sha256='5aaad7deea127a4790c8aa95c42fd9451ab10b5d6c68b226b92d4853002f438d')
    version('3.15.5', sha256='67dc31f1c1c941a0e45301ed4042628586e92e8c4e9b119695717ae782ef23a3')
    version('3.15.4', sha256='1e62fb0859a12891022765d1e24660cfcd704291c58667082d81a0618d6b0047')
    version('3.15.3', sha256='483028088020001e6f8d57b78a7fc880ed52d6693f57d627779c428f55cff73d')
    version('3.15.2', sha256='3b10c19c69fc42e01a38132668724a01f1da56f5c353105cd28f1120cc9041d8')
    version('3.15.1', sha256='c0ac6566e69d1d70b431e07e7598e9de95e84891c2452db1367c846b75109deb')
    version('3.15.0', sha256='ac46db6bfcaaec8cd28335231076815bd5438f401a4a05e33736b4f9ff12e59a')
    version('3.14.6', sha256='4de0c8820419fb15bc683b780127ff57067b62ca18749e864a87c6d7c93f1230')
    version('3.14.5', sha256='8b8ff5c4e10468f696803b354a502d690c7d25c19d694a7e10008a302fdbb048')
    version('3.14.4', sha256='b030969816e02c251a6d010c07a90b69ade44932f9ddfac3090ff5e95ab97d5c')
    version('3.14.3', sha256='63ed7e3440f2bbc732a6c44aa878364f88f5016ab375d9b36d742893a049053d')
    version('3.14.2', sha256='87a04fd05cac20a2ec47094b7d18b96e0651257d8c768ced2ef7db270ecfb9cb')
    version('3.14.1', sha256='0b4681165a9af96594c794b97ac6993452ec902726679f6b50bb450f89d230ed')
    version('3.14.0', sha256='a8f9caba03e0d57d8452c08505cf96be5f6949adaa266e819382162c03ddb9c5')
    version('3.13.6', sha256='67ca2cf3040d08fdc51d27f660ea3157732b24c2f47aae1b19d63f62a39842c2')
    version('3.13.5', sha256='10fc542dab961c8b17db35ad3a208cb184c237fc84e183817e38e6c7ab4b8732')
    version('3.13.4', sha256='8d470cba1ceb9638694550134a2f23aac85ed7249cb74992581210597d978b94')
    version('3.13.3', sha256='dc744895ee6b9c4491ff817bef0d3abd680c5e3c25e601be44240ce65ab4f337')
    version('3.13.2', sha256='6083422a7c5b8e89e5e4ccf64acade9bf8ab70245e25bca3a3da03caf74602f1')
    version('3.13.1', sha256='74a895e44e2ff1146838aaccb7613e7626d99e0eed64ca032c87c72d084efac3')
    version('3.13.0', sha256='f0ea543a54145c5d1387e25b121c3fd1b1ca834032c5a33f6f1d929e95bdf0e5')
    version('3.12.5', sha256='d676eb67e79314d6cca6422d7c477d2b192c830b89d5edc6b46934f7453bcfc0')
    version('3.12.4', sha256='56a941130da93bbacb3cfa74dcacea1e3cd8e36a0341f9ced09977b1457084c3')
    version('3.12.3', sha256='91f77d7b0f54056f085b9e27938922db3d9bb1734a2e2a6d26f43d3e6c0cf631')
    version('3.12.2', sha256='d874b2e198c4cb73551c2eca1d2c5d27da710be4d00517adb8f9eb3d6d0375e8')
    version('3.12.1', sha256='b72d895d0f4a79acb13ebc782b47b26d10d4e5706d399f533afcd5b3dba13737')
    version('3.12.0', sha256='ba9ecf69783c7ebf05bd1c91dd1d4b38bf09b7a2d5f9a774aa6bb46deff7cb14')
    version('3.11.4', sha256='319cb5a875a692a67fe5b1b90009ba8f182e21921ae645d38106544aff20c3c1')
    version('3.11.3', sha256='199ad9650a9f58603b49e7fff7cd003ceb03aa231e5d37d0bf0496c6348eca81')
    version('3.11.2', sha256='4d244dd7d1565d6534e776445fcf6977a6ee2a8bb2be4a36ac1e0fc1f9ad9cfa')
    version('3.11.1', sha256='cb627f99f7ce1540ebbbf338189f89a5f1ecf3ab3b5b0e357f9e46c209f1fb23')
    version('3.11.0', sha256='b3bed2a9263193c84138052a1b92d47299c3490dd24d1d0bf79fb884e71e678a')
    version('3.10.5', sha256='3a81c8406410e0ffa8a3e9f8efcdf2e683cc40613c9bb5cb378a6498f595803e')
    version('3.10.4', sha256='6c836df84caa9ae683ae401d3f94eb9471353156fec6db602bf2e857e4ec339f')
    version('3.10.3', sha256='cd106babbae091604fee40c258737c84dec048949be779eaef5a745df3dc8de4')
    version('3.10.2', sha256='9d3381bcf9c63abe6521b21a88efc70f8e893293503cff497971d0d9c1ec68cc')
    version('3.10.1', sha256='b6e64ce062113ee0e2e2a6cfffb4d33c085ec91d5bc3afeb33781074aa5a22a5')
    version('3.10.0', sha256='6ebacc010397ea47649495e8363cd7d7d86b876e6df07c6f6ccfa48b22fa555c')
    version('3.9.4', sha256='ecc647c9b1ef565a2c113936454c65632eedc1626e0fc99b5a36accb91195a63')
    version('3.9.3', sha256='6c7f2c7a28433385d74d647b4934aaeea3c1b3053b207973c9497639b6ebf7c8')
    version('3.9.2', sha256='ab396ae5dbfff808df1b5648f5ce30f3021ec70faec3d5cd63df324d416ac6ac')
    version('3.9.1', sha256='742e838a35d278693e956ed1ca4592c1d663451f6beea0694bf334aeb67681e8')
    version('3.9.0', sha256='dcbcab1f321667be1c6e5f8e7b4ee8670bb09e372e51f1ea6471464519d54b2d')
    version('3.8.4', sha256='9f78dc4dd4c58433fa18d3dd3a9029e39a83e4e4b64f845a029dd9fed44bc4c7')
    version('3.8.3', sha256='01f9c3ed937eafac6c9e006510b61c7cd07197115ec40c429fc835f346ca3eac')
    version('3.8.2', sha256='42690508d408e31fb98be738ac097bc869be14c5bfe08dda2184243283ceb16a')
    version('3.8.1', sha256='9b48a9e72d304046923667d2ab1f201778cc56242928a374ff9e074843a334ff')
    version('3.8.0', sha256='1e1b4d90ccbf98dc5759a956ac9a771310a6690f1cbb37b31502b29568262d7e')
    version('3.7.7', sha256='40fd3bc76998e056c4097704c08f28eb89bf3b93164dc9e69abab393f43bf6f0')
    version('3.7.6', sha256='3c8ee051349587d45baa7910c54ce8e0a571592e3b40f3054a7b7f986919d449')
    version('3.7.5', sha256='493ab0b6c1b3fe68e71d990eff87c84f499f680e6d2c0c394e78646a82ed4be3')
    version('3.7.4', sha256='54b804f924ea5be3b6718b4d4e98f8ccb9d1bd6bbbd1e9c0f18c4a90ddf5db18')
    version('3.7.2', sha256='36681dd0df97e0d5cd182d902e89f527eb8f441f05271159dac5340acb4cf0ec')
    version('3.6.4', sha256='eb09925a139b52b4dd5a071b3da4fe2165f1d6e8f71d410479603c9976c940f0')
    version('3.6.3', sha256='776e2644e4003653c56a44a6f7c02c41427af26f7c5cd9bec3aa84ed90223245')
    version('3.5.3', sha256='68e6a42f5ec75bad87f74d4df8f55ad63f0c4d996f162da6713cb3d6f566830d')
    version('3.5.2', sha256='1a8f09af654afab787c732e7b2f5d0c1d856777398148351565389d38d30935e')
    version('3.5.1', sha256='199af205f62dcc572728600670c7d4c8cb0d4efc4172c26f02b895d9dd1df245')
    version('3.4.4', sha256='fa73b99caf70c416a967234f5476cdb1d2c014610ee0619e48f54d8d309631b7')

    variant('shared',  default=True,
            description='Enables the build of shared libraries')
    variant('mpi',     default=True,  description='Activates MPI support')
    variant('double',  default=True,
            description='Switches between single and double precision')
    variant('complex', default=False, description='Build with complex numbers')
    variant('debug',   default=False, description='Compile in debug mode')

    variant('metis',   default=True,
            description='Activates support for metis and parmetis')
    variant('ptscotch',   default=False,
            description='Activates support for PTScotch (only parallel)')
    variant('hdf5',    default=True,
            description='Activates support for HDF5 (only parallel)')
    variant('hypre',   default=True,
            description='Activates support for Hypre (only parallel)')
    variant('hpddm',   default=False,
            description='Activates support for HPDDM (only parallel)')
    variant('mmg',   default=False,
            description='Activates support for MMG')
    variant('parmmg',   default=False,
            description='Activates support for ParMMG (only parallel)')
    variant('tetgen',   default=False,
            description='Activates support for Tetgen')
    # Mumps is disabled by default, because it depends on Scalapack
    # which is not portable to all HPC systems
    variant('mumps',   default=False,
            description='Activates support for MUMPS (only parallel)')
    variant('superlu-dist', default=True,
            description='Activates support for SuperluDist (only parallel)')
    variant('strumpack', default=False,
            description='Activates support for Strumpack')
    variant('scalapack', default=False,
            description='Activates support for Scalapack')
    variant('trilinos', default=False,
            description='Activates support for Trilinos (only parallel)')
    variant('mkl-pardiso', default=False,
            description='Activates support for MKL Pardiso')
    variant('int64', default=False,
            description='Compile with 64bit indices')
    variant('clanguage', default='C', values=('C', 'C++'),
            description='Specify C (recommended) or C++ to compile PETSc',
            multi=False)
    variant('fftw', default=False,
            description='Activates support for FFTW (only parallel)')
    variant('suite-sparse', default=False,
            description='Activates support for SuiteSparse')
    variant('knl', default=False,
            description='Build for KNL')
    variant('X', default=False,
            description='Activate X support')
    variant('batch', default=False,
            description='Enable when mpiexec is not available to run binaries')
    variant('valgrind', default=False,
            description='Enable Valgrind Client Request mechanism')
    variant('jpeg', default=False,
            description='Activates support for JPEG')
    variant('libpng', default=False,
            description='Activates support for PNG')
    variant('giflib', default=False,
            description='Activates support for GIF')
    variant('mpfr', default=False,
            description='Activates support for MPFR')
    variant('moab', default=False,
            description='Acivates support for MOAB (only parallel)')
    variant('random123', default=False,
            description='Activates support for Random123')
    variant('exodusii', default=False,
            description='Activates support for ExodusII (only parallel)')
    variant('cgns', default=False,
            description='Activates support for CGNS (only parallel)')
    variant('memkind', default=False,
            description='Activates support for Memkind')
    variant('p4est', default=False,
            description='Activates support for P4Est (only parallel)')
    variant('saws', default=False,
            description='Activates support for Saws')
    variant('libyaml', default=False,
            description='Activates support for YAML')
    variant('openmp', default=False,
            description='Activates support for openmp')
    variant('hwloc', default=False,
            description='Activates support for hwloc')
    variant('kokkos', default=False,
            description='Activates support for kokkos and kokkos-kernels')

    # 3.8.0 has a build issue with MKL - so list this conflict explicitly
    conflicts('^intel-mkl', when='@3.8.0')

    # These require +mpi
    mpi_msg = 'Requires +mpi'
    conflicts('+cgns', when='~mpi', msg=mpi_msg)
    conflicts('+exodusii', when='~mpi', msg=mpi_msg)
    conflicts('+fftw', when='~mpi', msg=mpi_msg)
    conflicts('+hdf5', when='~mpi', msg=mpi_msg)
    conflicts('+hypre', when='~mpi', msg=mpi_msg)
    conflicts('+hpddm', when='~mpi', msg=mpi_msg)
    conflicts('+parmmg', when='~mpi', msg=mpi_msg)
    conflicts('+moab', when='~mpi', msg=mpi_msg)
    conflicts('+mumps', when='~mpi', msg=mpi_msg)
    conflicts('+p4est', when='~mpi', msg=mpi_msg)
    conflicts('+ptscotch', when='~mpi', msg=mpi_msg)
    conflicts('+superlu-dist', when='~mpi', msg=mpi_msg)
    conflicts('+trilinos', when='~mpi', msg=mpi_msg)
    conflicts('+kokkos', when='~mpi', msg=mpi_msg)
    conflicts('^openmpi~cuda', when='+cuda')  # +cuda requires CUDA enabled OpenMPI

    # older versions of petsc did not support mumps when +int64
    conflicts('+mumps', when='@:3.12+int64')

    filter_compiler_wrappers(
        'petscvariables', relative_root='lib/petsc/conf'
    )

    # temporary workaround Clang 8.1.0 with XCode 8.3 on macOS, see
    # https://bitbucket.org/petsc/petsc/commits/4f290403fdd060d09d5cb07345cbfd52670e3cbc
    # the patch is an adaptation of the original commit to 3.7.5
    patch('macos-clang-8.1.0.diff', when='@3.7.5%apple-clang@8.1.0:')
    patch('pkg-config-3.7.6-3.8.4.diff', when='@3.7.6:3.8.4')
    patch('xcode_stub_out_of_sync.patch', when='@:3.10.4')
    patch('xlf_fix-dup-petscfecreate.patch', when='@3.11.0')
    patch('disable-DEPRECATED_ENUM.diff', when='@3.14.1 +cuda')

    depends_on('diffutils', type='build')

    # Virtual dependencies
    # Git repository needs sowing to build Fortran interface
    depends_on('sowing', when='@main')

    # PETSc, hypre, superlu_dist when built with int64 use 32 bit integers
    # with BLAS/LAPACK
    depends_on('blas')
    depends_on('lapack')
    depends_on('mpi', when='+mpi')
    depends_on('cuda', when='+cuda')
    depends_on('hip', when='+rocm')
    depends_on('hipblas', when='+rocm')
    depends_on('hipsparse', when='+rocm')
    depends_on('rocsparse', when='+rocm')
    depends_on('rocsolver', when='+rocm')
    depends_on('rocblas', when='+rocm')
    depends_on('rocrand', when='+rocm')
    depends_on('rocthrust', when='+rocm')
    depends_on('rocprim', when='+rocm')

    # Build dependencies
    depends_on('python@2.6:2.8', type='build', when='@:3.10')
    depends_on('python@2.6:2.8,3.4:', type='build', when='@3.11:')

    # Other dependencies
    depends_on('metis@5:~int64+real64', when='@:3.7+metis~int64+double')
    depends_on('metis@5:~int64', when='@:3.7+metis~int64~double')
    depends_on('metis@5:+int64+real64', when='@:3.7+metis+int64+double')
    depends_on('metis@5:+int64', when='@:3.7+metis+int64~double')
    # petsc-3.8+ uses default (float) metis with any (petsc) precision
    depends_on('metis@5:~int64', when='@3.8:+metis~int64')
    depends_on('metis@5:+int64', when='@3.8:+metis+int64')

    # PTScotch: Currently disable Parmetis wrapper, this means
    # nested disection won't be available thought PTScotch
    depends_on('scotch+esmumps~metis+mpi', when='+ptscotch')
    depends_on('scotch+int64', when='+ptscotch+int64')

    depends_on('hdf5@:1.10+mpi', when='@:3.12+hdf5+mpi')
    depends_on('hdf5+mpi', when='@3.13:+hdf5+mpi')
    depends_on('hdf5+mpi', when='+exodusii+mpi')
    depends_on('hdf5+mpi', when='+cgns+mpi')
    depends_on('zlib', when='+hdf5')
    depends_on('zlib', when='+libpng')
    depends_on('zlib', when='+p4est')
    depends_on('parmetis+int64', when='+metis+mpi+int64')
    depends_on('parmetis~int64', when='+metis+mpi~int64')
    depends_on('valgrind', when='+valgrind')
    depends_on('mmg', when='+mmg')
    depends_on('parmmg', when='+parmmg')
    depends_on('tetgen+pic', when='+tetgen')
    # Hypre does not support complex numbers.
    # Also PETSc prefer to build it without internal superlu, likely due to
    # conflict in headers see
    # https://bitbucket.org/petsc/petsc/src/90564b43f6b05485163c147b464b5d6d28cde3ef/config/BuildSystem/config/packages/hypre.py
    depends_on('hypre@:2.13+mpi~internal-superlu~int64', when='@:3.8+hypre+mpi~complex~int64')
    depends_on('hypre@:2.13+mpi~internal-superlu+int64', when='@:3.8+hypre+mpi~complex+int64')
    depends_on('hypre@2.14:2.18.2+mpi~internal-superlu~int64', when='@3.9:3.13+hypre+mpi~complex~int64')
    depends_on('hypre@2.14:2.18.2+mpi~internal-superlu+int64', when='@3.9:3.13+hypre+mpi~complex+int64')
    depends_on('hypre@2.14:2.22.0+mpi~internal-superlu~int64', when='@3.14:3.15+hypre+mpi~complex~int64')
    depends_on('hypre@2.14:2.22.0+mpi~internal-superlu+int64', when='@3.14:3.15+hypre+mpi~complex+int64')
    depends_on('hypre@2.14:+mpi~internal-superlu~int64', when='@3.16:+hypre+mpi~complex~int64')
    depends_on('hypre@2.14:+mpi~internal-superlu+int64', when='@3.16:+hypre+mpi~complex+int64')
    depends_on('hypre@develop+mpi~internal-superlu+int64', when='@main+hypre+mpi~complex+int64')
    depends_on('hypre@develop+mpi~internal-superlu~int64', when='@main+hypre+mpi~complex~int64')
    depends_on('superlu-dist@:4.3~int64', when='@3.4.4:3.6.4+superlu-dist+mpi~int64')
    depends_on('superlu-dist@:4.3+int64', when='@3.4.4:3.6.4+superlu-dist+mpi+int64')
    depends_on('superlu-dist@5.0.0:5.1.3~int64', when='@3.7.0:3.7+superlu-dist+mpi~int64')
    depends_on('superlu-dist@5.0.0:5.1.3+int64', when='@3.7.0:3.7+superlu-dist+mpi+int64')
    depends_on('superlu-dist@5.2.0:5.2~int64', when='@3.8:3.9+superlu-dist+mpi~int64')
    depends_on('superlu-dist@5.2.0:5.2+int64', when='@3.8:3.9+superlu-dist+mpi+int64')
    depends_on('superlu-dist@5.4.0:5.4~int64', when='@3.10:3.10.2+superlu-dist+mpi~int64')
    depends_on('superlu-dist@5.4.0:5.4+int64', when='@3.10:3.10.2+superlu-dist+mpi+int64')
    depends_on('superlu-dist@6.1.0:6.1~int64', when='@3.10.3:3.12+superlu-dist+mpi~int64')
    depends_on('superlu-dist@6.1.0:6.1+int64', when='@3.10.3:3.12+superlu-dist+mpi+int64')
    depends_on('superlu-dist@6.1:~int64', when='@3.13.0:+superlu-dist+mpi~int64')
    depends_on('superlu-dist@6.1:+int64', when='@3.13.0:+superlu-dist+mpi+int64')
    depends_on('superlu-dist@develop~int64', when='@main+superlu-dist+mpi~int64')
    depends_on('superlu-dist@develop+int64', when='@main+superlu-dist+mpi+int64')
    depends_on('strumpack', when='+strumpack')
    depends_on('scalapack', when='+strumpack')
    depends_on('metis', when='+strumpack')
    depends_on('scalapack', when='+scalapack')
    depends_on('mumps+mpi~int64~metis~parmetis~openmp', when='+mumps~metis~openmp')
    depends_on('mumps+mpi~int64+metis+parmetis~openmp', when='+mumps+metis~openmp')
    depends_on('mumps+mpi~int64~metis~parmetis+openmp', when='+mumps~metis+openmp')
    depends_on('mumps+mpi~int64+metis+parmetis+openmp', when='+mumps+metis+openmp')
    depends_on('scalapack', when='+mumps')
    depends_on('trilinos@12.6.2:+mpi', when='@3.7.0:+trilinos+mpi')
    depends_on('trilinos@develop+mpi', when='@main+trilinos+mpi')
    depends_on('mkl', when='+mkl-pardiso')
    depends_on('fftw+mpi', when='+fftw+mpi')
    depends_on('suite-sparse', when='+suite-sparse')
    depends_on('libx11', when='+X')
    depends_on('mpfr', when='+mpfr')
    depends_on('gmp', when='+mpfr')
    depends_on('jpeg', when='+jpeg')
    depends_on('libpng', when='+libpng')
    depends_on('giflib', when='+giflib')
    depends_on('exodusii+mpi', when='+exodusii+mpi')
    depends_on('netcdf-c+mpi', when='+exodusii+mpi')
    depends_on('parallel-netcdf', when='+exodusii+mpi')
    depends_on('random123', when='+random123')
    depends_on('moab+mpi', when='+moab+mpi')
    depends_on('cgns+mpi', when='+cgns+mpi')
    depends_on('memkind', when='+memkind')
    depends_on('p4est+mpi', when='+p4est+mpi')
    depends_on('saws', when='+saws')
    depends_on('libyaml', when='+libyaml')
    depends_on('hwloc', when='+hwloc')
    depends_on('kokkos', when='+kokkos')
    depends_on('kokkos-kernels', when='+kokkos')
    depends_on('kokkos+cuda+wrapper+cuda_lambda', when='+kokkos +cuda')
    depends_on('kokkos-kernels+cuda', when='+kokkos +cuda')
    depends_on('kokkos+rocm', when='+kokkos +rocm')

    # Using the following tarballs
    # * petsc-3.12 (and older) - includes docs
    # * petsc-lite-3.13, petsc-lite-3.14 (without docs)
    # * petsc-3.15 and newer (without docs)
    def url_for_version(self, version):
        if self.spec.satisfies('@3.13.0:3.14.6'):
            return "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-lite-{0}.tar.gz".format(version)
        else:
            return "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-{0}.tar.gz".format(version)

    def mpi_dependent_options(self):
        if '~mpi' in self.spec:
            compiler_opts = [
                '--with-cc=%s' % os.environ['CC'],
                '--with-cxx=%s' % (os.environ['CXX']
                                   if self.compiler.cxx is not None else '0'),
                '--with-fc=%s' % (os.environ['FC']
                                  if self.compiler.fc is not None else '0'),
                '--with-mpi=0'
            ]
        else:
            compiler_opts = [
                '--with-cc=%s' % self.spec['mpi'].mpicc,
                '--with-cxx=%s' % self.spec['mpi'].mpicxx,
                '--with-fc=%s' % self.spec['mpi'].mpifc,
            ]
            if self.spec.satisfies('%intel'):
                # mpiifort needs some help to automatically link
                # all necessary run-time libraries
                compiler_opts.append('--FC_LINKER_FLAGS=-lintlc')
        return compiler_opts

    def install(self, spec, prefix):
        options = ['--with-ssl=0',
                   '--download-c2html=0',
                   '--download-sowing=0',
                   '--download-hwloc=0',
                   'CFLAGS=%s' % ' '.join(spec.compiler_flags['cflags']),
                   'FFLAGS=%s' % ' '.join(spec.compiler_flags['fflags']),
                   'CXXFLAGS=%s' % ' '.join(spec.compiler_flags['cxxflags'])]
        options.extend(self.mpi_dependent_options())
        options.extend([
            '--with-precision=%s' % (
                'double' if '+double' in spec else 'single'),
            '--with-scalar-type=%s' % (
                'complex' if '+complex' in spec else 'real'),
            '--with-shared-libraries=%s' % ('1' if '+shared' in spec else '0'),
            '--with-debugging=%s' % ('1' if '+debug' in spec else '0'),
            '--with-openmp=%s' % ('1' if '+openmp' in spec else '0'),
            '--with-64-bit-indices=%s' % ('1' if '+int64' in spec else '0')
        ])
        if '+debug' not in spec:
            options.extend(['COPTFLAGS=',
                            'FOPTFLAGS=',
                            'CXXOPTFLAGS='])

        # Make sure we use exactly the same Blas/Lapack libraries
        # across the DAG. To that end list them explicitly
        lapack_blas = spec['lapack'].libs + spec['blas'].libs
        options.extend([
            '--with-blas-lapack-lib=%s' % lapack_blas.joined()
        ])

        if '+batch' in spec:
            options.append('--with-batch=1')
        if '+knl' in spec:
            options.append('--with-avx-512-kernels')
            options.append('--with-memalign=64')
        if '+X' in spec:
            options.append('--with-x=1')
        else:
            options.append('--with-x=0')

        if 'trilinos' in spec:
            if spec.satisfies('^trilinos+boost'):
                options.append('--with-boost=1')

        if self.spec.satisfies('clanguage=C++'):
            options.append('--with-clanguage=C++')
        else:
            options.append('--with-clanguage=C')

        # Activates library support if needed (i.e. direct dependency)
        jpeg_sp = spec['jpeg'].name if 'jpeg' in spec else 'jpeg'
        scalapack_sp = spec['scalapack'].name if 'scalapack' in spec else 'scalapack'

        # tuple format (spacklibname, petsclibname, useinc, uselib)
        # default: 'gmp', => ('gmp', 'gmp', True, True)
        # any other combination needs a full tuple
        # if not (useinc || uselib): usedir - i.e (False, False)
        direct_dependencies = [x.name for x in spec.dependencies()]
        for library in (
                ('cuda', 'cuda', False, False),
                ('hip', 'hip', True, False),
                'metis',
                'hypre',
                'parmetis',
                ('kokkos', 'kokkos', False, False),
                ('kokkos-kernels', 'kokkos-kernels', False, False),
                ('superlu-dist', 'superlu_dist', True, True),
                ('scotch', 'ptscotch', True, True),
                ('suite-sparse:umfpack,klu,cholmod,btf,ccolamd,colamd,camd,amd, \
                suitesparseconfig,spqr', 'suitesparse', True, True),
                ('hdf5:hl,fortran', 'hdf5', True, True),
                'zlib',
                'mumps',
                ('trilinos', 'trilinos', False, False),
                ('fftw:mpi', 'fftw', True, True),
                ('valgrind', 'valgrind', False, False),
                'gmp',
                'libpng',
                ('giflib', 'giflib', False, False),
                'mpfr',
                ('netcdf-c', 'netcdf', True, True),
                ('parallel-netcdf', 'pnetcdf', True, True),
                ('moab', 'moab', False, False),
                ('random123', 'random123', False, False),
                'exodusii',
                'cgns',
                'memkind',
                'p4est',
                ('saws', 'saws', False, False),
                ('libyaml', 'yaml', True, True),
                'hwloc',
                (jpeg_sp, 'libjpeg', True, True),
                (scalapack_sp, 'scalapack', False, True),
                'strumpack',
                'mmg',
                'parmmg',
                ('tetgen', 'tetgen', False, False),
        ):
            # Cannot check `library in spec` because of transitive deps
            # Cannot check variants because parmetis keys on +metis
            if isinstance(library, tuple):
                spacklibname, petsclibname, useinc, uselib = library
            else:
                spacklibname = library
                petsclibname = library
                useinc = True
                uselib = True

            library_requested = spacklibname.split(':')[0] in direct_dependencies
            options.append(
                '--with-{library}={value}'.format(
                    library=petsclibname,
                    value=('1' if library_requested else '0'))
            )
            if library_requested:
                if useinc or uselib:
                    if useinc:
                        options.append(
                            '--with-{library}-include={value}'.format(
                                library=petsclibname,
                                value=spec[spacklibname].prefix.include)
                        )
                    if uselib:
                        options.append(
                            '--with-{library}-lib={value}'.format(
                                library=petsclibname,
                                value=spec[spacklibname].libs.joined())
                        )
                else:
                    options.append(
                        '--with-{library}-dir={path}'.format(
                            library=petsclibname, path=spec[spacklibname].prefix)
                    )

        if '+cuda' in spec:
            if not spec.satisfies('cuda_arch=none'):
                cuda_arch = spec.variants['cuda_arch'].value
                if spec.satisfies('@3.14:'):
                    options.append('--with-cuda-gencodearch={0}'.format(cuda_arch[0]))
                else:
                    options.append('CUDAFLAGS=-gencode arch=compute_{0},code=sm_{0}'
                                   .format(cuda_arch[0]))
        if '+rocm' in spec:
            if not spec.satisfies('amdgpu_target=none'):
                hip_arch = spec.variants['amdgpu_target'].value
                options.append('--with-hip-arch={0}'.format(hip_arch[0]))
            hip_pkgs = ['hipsparse', 'hipblas', 'rocsparse', 'rocsolver', 'rocblas']
            hip_ipkgs = hip_pkgs + ['rocthrust', 'rocprim']
            hip_lpkgs = hip_pkgs + ['rocrand']
            hip_inc = ''
            hip_lib = ''
            for pkg in hip_ipkgs:
                hip_inc += spec[pkg].headers.include_flags + ' '
            for pkg in hip_lpkgs:
                hip_lib += spec[pkg].libs.joined() + ' '
            options.append('HIPPPFLAGS=%s' % hip_inc)
            options.append('with-hip-lib=%s -L%s -lamdhip64' %
                           (hip_lib, spec['hip'].prefix.lib))

        if 'superlu-dist' in spec:
            if spec.satisfies('@3.10.3:3.15'):
                options.append('--with-cxx-dialect=C++11')

        if '+mkl-pardiso' in spec:
            options.append(
                '--with-mkl_pardiso-dir=%s' % spec['mkl'].prefix
            )

        # For the moment, HPDDM does not work as a dependency
        # using download instead
        if '+hpddm' in spec:
            options.append('--download-hpddm')

        # revert changes by kokkos-nvcc-wrapper
        if spec.satisfies('^kokkos+cuda+wrapper'):
            env['MPICH_CXX'] = env['CXX']
            env['OMPI_CXX'] = env['CXX']
            env['MPICXX_CXX'] = env['CXX']

        python('configure', '--prefix=%s' % prefix, *options)

        # PETSc has its own way of doing parallel make.
        make('V=1 MAKE_NP=%s' % make_jobs, parallel=False)
        make("install")

        if self.run_tests:
            make('check PETSC_ARCH="" PETSC_DIR={0}'.format(self.prefix),
                 parallel=False)

    def setup_build_environment(self, env):
        # configure fails if these env vars are set outside of Spack
        env.unset('PETSC_DIR')
        env.unset('PETSC_ARCH')

    def setup_run_environment(self, env):
        # Set PETSC_DIR in the module file
        env.set('PETSC_DIR', self.prefix)
        env.unset('PETSC_ARCH')

    def setup_dependent_build_environment(self, env, dependent_spec):
        # Set up PETSC_DIR for everyone using PETSc package
        env.set('PETSC_DIR', self.prefix)
        env.unset('PETSC_ARCH')

    @property
    def archive_files(self):
        return [join_path(self.stage.source_path, 'configure.log'),
                join_path(self.stage.source_path, 'make.log')]

    @property
    def headers(self):
        return find_headers('petsc', self.prefix.include, recursive=False) \
            or None  # return None to indicate failure

    # For the 'libs' property - use the default handler.

    @run_after('install')
    def setup_build_tests(self):
        """Copy the build test files after the package is installed to an
        install test subdirectory for use during `spack test run`."""
        self.cache_extra_test_sources('src/ksp/ksp/tutorials')
        self.cache_extra_test_sources('src/snes/tutorials')

    def test(self):
        # solve Poisson equation in 2D to make sure nothing is broken:
        spec = self.spec
        env['PETSC_DIR'] = self.prefix
        env['PETSC_ARCH'] = ''
        if ('+mpi' in spec):
            runexe = Executable(join_path(spec['mpi'].prefix.bin,
                                          'mpiexec')).command
            runopt = ['-n', '4']
        else:
            runexe = Executable(join_path(self.prefix,
                                          'lib/petsc/bin/petsc-mpiexec.uni')).command
            runopt = ['-n', '1']
        w_dir = join_path(self.install_test_root, 'src/ksp/ksp/tutorials')
        with working_dir(w_dir):
            testexe = ['ex50', '-da_grid_x', '4', '-da_grid_y', '4']
            testdict = {
                None: [],
                '+superlu-dist':
                ['-pc_type', 'lu', '-pc_factor_mat_solver_type', 'superlu_dist'],
                '+mumps':
                ['-pc_type', 'lu', '-pc_factor_mat_solver_type', 'mumps'],
                '+hypre':
                ['-pc_type', 'hypre', '-pc_hypre_type', 'boomeramg'],
                '+mkl-pardiso':
                ['-pc_type', 'lu', '-pc_factor_mat_solver_type', 'mkl_pardiso'],
            }
            make('ex50', parallel=False)
            for feature, featureopt in testdict.items():
                if not feature or feature in spec:
                    self.run_test(runexe, runopt + testexe + featureopt)
            if '+cuda' in spec:
                make('ex7', parallel=False)
                testexe = ['ex7', '-mat_type', 'aijcusparse',
                           '-sub_pc_factor_mat_solver_type', 'cusparse',
                           '-sub_ksp_type', 'preonly', '-sub_pc_type', 'ilu',
                           '-use_gpu_aware_mpi', '0']
                self.run_test(runexe, runopt + testexe)
            make('clean', parallel=False)
        w_dir = join_path(self.install_test_root, 'src/snes/tutorials')
        with working_dir(w_dir):
            if '+kokkos' in spec:
                make('ex3k', parallel=False)
                testexe = ['ex3k', '-view_initial', '-dm_vec_type', 'kokkos',
                           '-dm_mat_type', 'aijkokkos', '-use_gpu_aware_mpi', '0',
                           '-snes_monitor']
                self.run_test(runexe, runopt + testexe)
            make('clean', parallel=False)

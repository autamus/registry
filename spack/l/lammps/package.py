# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import datetime as dt


class Lammps(CMakePackage, CudaPackage):
    """LAMMPS stands for Large-scale Atomic/Molecular Massively
    Parallel Simulator. This package uses patch releases, not
    stable release.
    See https://github.com/spack/spack/pull/5342 for a detailed
    discussion.
    """
    homepage = "http://lammps.sandia.gov/"
    url      = "https://github.com/lammps/lammps/archive/patch_1Sep2017.tar.gz"
    git      = "https://github.com/lammps/lammps.git"

    tags = ['ecp', 'ecp-apps']
    version('29.Oct.2020', sha256='5d88d4e92f4e0bb57c8ab30e0d20de556830af820223778b9967bec2184efd46', url='https://github.com/lammps/lammps/archive/patch_1Sep2017.tar.gz')

    def url_for_version(self, version):
        vdate = dt.datetime.strptime(str(version), "%Y%m%d")
        return "https://github.com/lammps/lammps/archive/patch_{0}.tar.gz".format(
            vdate.strftime("%d%b%Y").lstrip('0'))

    supported_packages = ['asphere', 'body', 'class2', 'colloid', 'compress',
                          'coreshell', 'dipole', 'granular', 'kspace',
                          'kokkos', 'latte', 'manybody', 'mc', 'meam', 'misc',
                          'mliap', 'molecule', 'mpiio', 'opt', 'peri', 'poems',
                          'python', 'qeq', 'replica', 'rigid', 'shock', 'snap',
                          'spin', 'srd', 'user-atc', 'user-adios',
                          'user-awpmd', 'user-bocs', 'user-cgsdk',
                          'user-colvars', 'user-diffraction', 'user-dpd',
                          'user-drude', 'user-eff', 'user-fep', 'user-h5md',
                          'user-lb', 'user-manifold', 'user-meamc',
                          'user-mesodpd', 'user-mesont', 'user-mgpt',
                          'user-misc', 'user-mofff', 'user-netcdf', 'user-omp',
                          'user-phonon', 'user-plumed', 'user-ptm', 'user-qtb',
                          'user-reaction', 'user-reaxc', 'user-sdpd',
                          'user-smd', 'user-smtbq', 'user-sph', 'user-tally',
                          'user-uef', 'user-yaff', 'voronoi']

    for pkg in supported_packages:
        variant(pkg, default=False,
                description='Activate the {0} package'.format(pkg))
    variant('lib', default=True,
            description='Build the liblammps in addition to the executable')
    variant('mpi', default=True,
            description='Build with mpi')
    variant('jpeg', default=True,
            description='Build with jpeg support')
    variant('png', default=True,
            description='Build with png support')
    variant('ffmpeg', default=True,
            description='Build with ffmpeg support')
    variant('kim', default=True,
            description='Build with KIM support')
    variant('openmp', default=True, description='Build with OpenMP')
    variant('opencl', default=False, description='Build with OpenCL')
    variant('exceptions', default=False,
            description='Build with lammps exceptions')
    variant('cuda_mps', default=False,
            description='(CUDA only) Enable tweaks for running ' +
                        'with Nvidia CUDA Multi-process services daemon')

    depends_on('mpi', when='+mpi')
    depends_on('mpi', when='+mpiio')
    depends_on('fftw-api@3', when='+kspace')
    depends_on('voropp+pic', when='+voronoi')
    depends_on('netcdf-c+mpi', when='+user-netcdf')
    depends_on('blas', when='+user-atc')
    depends_on('lapack', when='+user-atc')
    depends_on('opencl', when='+opencl')
    depends_on('latte@1.0.1', when='@:20180222+latte')
    depends_on('latte@1.1.1:', when='@20180316:20180628+latte')
    depends_on('latte@1.2.1:', when='@20180629:20200505+latte')
    depends_on('latte@1.2.2:', when='@20200602:+latte')
    depends_on('blas', when='+latte')
    depends_on('lapack', when='+latte')
    depends_on('python', when='+python')
    depends_on('mpi', when='+user-lb')
    depends_on('mpi', when='+user-h5md')
    depends_on('hdf5', when='+user-h5md')
    depends_on('jpeg', when='+jpeg')
    depends_on('kim-api', when='+kim')
    depends_on('libpng', when='+png')
    depends_on('ffmpeg', when='+ffmpeg')
    depends_on('kokkos+deprecated_code+shared@3.0', when='@20200303+kokkos')
    depends_on('kokkos+shared@3.1:', when='@20200505:+kokkos')
    depends_on('adios2', when='+user-adios')
    depends_on('plumed', when='+user-plumed')
    depends_on('eigen@3:', when='+user-smd')

    conflicts('+cuda', when='+opencl')
    conflicts('+body', when='+poems@:20180628')
    conflicts('+latte', when='@:20170921')
    conflicts('+python', when='~lib')
    conflicts('+qeq', when='~manybody')
    conflicts('+user-atc', when='~manybody')
    conflicts('+user-misc', when='~manybody')
    conflicts('+user-phonon', when='~kspace')
    conflicts('+user-misc', when='~manybody')
    conflicts('%gcc@9:', when='@:20200303+openmp')
    conflicts('+kokkos', when='@:20200227')
    conflicts(
        '+meam', when='@20181212:',
        msg='+meam was removed after @20181212, use +user-meamc instead')
    conflicts(
        '+user-meamc', when='@:20181212',
        msg='+user-meamc only added @20181212, use +meam instead')
    conflicts(
        '+user-reaction', when='@:20200303',
        msg='+user-reaction only supported for version 20200505 and later')
    conflicts('+mliap', when='~snap')
    conflicts(
        '+adios +mpi', when='^adios2~mpi',
        msg='With +adios, mpi setting for adios2 and lammps must be the same')
    conflicts(
        '+adios ~mpi', when='^adios2+mpi',
        msg='With +adios, mpi setting for adios2 and lammps must be the same')

    patch("lib.patch", when="@20170901")
    patch("660.patch", when="@20170922")
    patch("https://github.com/lammps/lammps/commit/562300996285fdec4ef74542383276898555af06.patch",
          sha256="7e1610dad4d8203b45ca6dc2c1f97d02a40f98a5e9778f51a3dbcc30ea1dc717",
          when="@20200721 +cuda")

    root_cmakelists_dir = 'cmake'

    def cmake_args(self):
        spec = self.spec

        mpi_prefix = 'ENABLE'
        pkg_prefix = 'ENABLE'
        if spec.satisfies('@20180629:'):
            mpi_prefix = 'BUILD'
            pkg_prefix = 'PKG'

        args = [
            '-DBUILD_SHARED_LIBS={0}'.format(
                'ON' if '+lib' in spec else 'OFF'),
            '-DLAMMPS_EXCEPTIONS={0}'.format(
                'ON' if '+exceptions' in spec else 'OFF'),
            '-D{0}_MPI={1}'.format(
                mpi_prefix,
                'ON' if '+mpi' in spec else 'OFF'),
            '-DBUILD_OMP={0}'.format(
                'ON' if '+openmp' in spec else 'OFF'),
        ]
        if spec.satisfies('+cuda'):
            args.append('-DPKG_GPU=ON')
            args.append('-DGPU_API=cuda')
            cuda_arch = spec.variants['cuda_arch'].value
            if cuda_arch != 'none':
                args.append('-DGPU_ARCH=sm_{0}'.format(cuda_arch[0]))
            args.append('-DCUDA_MPS_SUPPORT={0}'.format(
                'ON' if '+cuda_mps' in spec else 'OFF'))
        elif spec.satisfies('+opencl'):
            args.append('-DPKG_GPU=ON')
            args.append('-DGPU_API=opencl')
        else:
            args.append('-DPKG_GPU=OFF')

        if spec.satisfies('@20180629:+lib'):
            args.append('-DBUILD_LIB=ON')

        args.append('-DWITH_JPEG={0}'.format(
            'ON' if '+jpeg' in spec else 'OFF'))
        args.append('-DWITH_PNG={0}'.format(
            'ON' if '+png' in spec else 'OFF'))
        args.append('-DWITH_FFMPEG={0}'.format(
            'ON' if '+ffmpeg' in spec else 'OFF'))

        for pkg in self.supported_packages:
            opt = '-D{0}_{1}'.format(pkg_prefix, pkg.upper())
            if '+{0}'.format(pkg) in spec:
                args.append('{0}=ON'.format(opt))
            else:
                args.append('{0}=OFF'.format(opt))
        if '+kim' in spec:
            args.append('-DPKG_KIM=ON')
        if '+kspace' in spec:
            if '^fftw' in spec:
                args.append('-DFFT=FFTW3')
            if '^mkl' in spec:
                args.append('-DFFT=MKL')
            if '^amdfftw' in spec:
                fftw_prefix = spec['amdfftw'].prefix
                args.append('-DFFTW_HOME={0}'.format(fftw_prefix))
                args.append('-DFFTW_INCLUDE_DIRS={0}'
                            .format(fftw_prefix.include))
                args.append('-DFFTW_LIBRARY_DIRS={0}'.format(fftw_prefix.lib))
        if '+kokkos' in spec:
            args.append('-DEXTERNAL_KOKKOS=ON')
        if '+user-adios' in spec:
            args.append('-DADIOS2_DIR={0}'.format(self.spec['adios2'].prefix))
        if '+user-plumed' in spec:
            args.append('-DDOWNLOAD_PLUMED=no')
            if '+shared' in self.spec['plumed']:
                args.append('-DPLUMED_MODE=shared')
            else:
                args.append('-DPLUMED_MODE=static')
        if '+user-smd' in spec:
            args.append('-DDOWNLOAD_EIGEN3=no')
            args.append('-DEIGEN3_INCLUDE_DIR={0}'.format(
                self.spec['eigen'].prefix.include))

        return args

    def setup_run_environment(self, env):
        env.set('LAMMPS_POTENTIALS',
                self.prefix.share.lammps.potentials)

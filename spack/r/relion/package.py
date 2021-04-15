# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Relion(CMakePackage, CudaPackage):
    """RELION (for REgularised LIkelihood OptimisatioN, pronounce rely-on) is a
    stand-alone computer program that employs an empirical Bayesian approach to
    refinement of (multiple) 3D reconstructions or 2D class averages in
    electron cryo-microscopy (cryo-EM)."""

    homepage = "http://http://www2.mrc-lmb.cam.ac.uk/relion"
    git      = "https://github.com/3dem/relion.git"
    url      = "https://github.com/3dem/relion/archive/3.1.0.zip"

    version('3.1.1', sha256='63e9b77e1ba9ec239375020ad6ff631424d1a5803cba5c608c09fd44d20b1618')
    version('3.1.0', sha256='8a7e751fa6ebcdf9f36046499b3d88e170c4da86d5ff9ad1914b5f3d178867a8')

    # 3.0.8 latest release in 3.0 branch
    version('3.0.8', sha256='18cdd58e3a612d32413eb37e473fe8fbf06262d2ed72e42da20356f459260973')
    version('3.0.7', sha256='a6d37248fc4d0bfc18f4badb7986dc1b6d6849baa2128b0b4dade13cb6991a99')

    # relion master contains development code
    # contains 3.0 branch code
    version('master')

    variant('gui', default=True, description="build the gui")
    variant('cuda', default=True, description="enable compute on gpu")
    variant('double', default=True, description="double precision (cpu) code")
    variant('double-gpu', default=False, description="double precision gpu")
    # if built with purpose=cluster then relion will link to gpfs libraries
    # if that's not desirable then use purpose=desktop
    variant('purpose', default='cluster', values=('cluster', 'desktop'),
            description="build relion for use in cluster or desktop")
    variant('build_type', default='RelWithDebInfo',
            description='The build type to build',
            values=('Debug', 'Release', 'RelWithDebInfo',
                    'Profiling', 'Benchmarking'))
    variant('mklfft', default=True, description='Use MKL rather than FFTW for FFT')
    variant('allow_ctf_in_sagd', default=True, description='Allow CTF-modulation in SAGD, as specified in Claim 1 of patent US10,282,513B2')

    depends_on('mpi')
    depends_on('cmake@3:', type='build')
    depends_on('fftw precision=float,double', when='~mklfft')
    depends_on('fltk', when='+gui')
    depends_on('libtiff')

    depends_on('cuda', when='+cuda')
    depends_on('cuda@9:', when='@3: +cuda')
    depends_on('tbb', when='~cuda')
    depends_on('mkl', when='~cuda +mklfft')

    patch('0002-Simple-patch-to-fix-intel-mkl-linking.patch', when='@:3.1.1 os=ubuntu18.04')

    def cmake_args(self):

        carch = self.spec.variants['cuda_arch'].value[0]

        args = [
            '-DCMAKE_C_FLAGS=-g',
            '-DCMAKE_CXX_FLAGS=-g',
            '-DGUI=%s' % ('+gui' in self.spec),
            '-DDoublePrec_CPU=%s' % ('+double' in self.spec),
            '-DDoublePrec_GPU=%s' % ('+double-gpu' in self.spec),
            '-DALLOW_CTF_IN_SAGD=%s' % ('+allow_ctf_in_sagd' in self.spec),
        ]

        if '+cuda' in self.spec:
            # relion+cuda requires selecting cuda_arch
            if not carch:
                raise ValueError("select cuda_arch when building with +cuda")
            else:
                args += ['-DCUDA=ON', '-DCudaTexture=ON',
                         '-DCUDA_ARCH=%s' % (carch)]

        # these new values were added in relion 3
        # do not seem to cause problems with < 3
        else:
            args += ['-DMKLFFT=%s' % ('+mklfft' in self.spec), '-DALTCPU=ON']

        return args

    def patch(self):
        # Remove flags not recognized by the NVIDIA compilers
        if self.spec.satisfies('%nvhpc'):
            filter_file('-std=c99', '-c99', 'src/apps/CMakeLists.txt')

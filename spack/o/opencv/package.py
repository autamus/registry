# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
class Opencv(CMakePackage, CudaPackage):
    """OpenCV (Open Source Computer Vision Library) is an open source computer
    vision and machine learning software library."""

    homepage = 'https://opencv.org/'
    url      = "https://github.com/opencv/opencv/archive/4.5.2.tar.gz"
    git      = 'https://github.com/opencv/opencv.git'

    maintainers = ['bvanessen', 'adamjstewart']
    version('4.5.2', sha256='ae258ed50aa039279c3d36afdea5c6ecf762515836b27871a8957c610d0424f8', url='https://github.com/opencv/opencv/archive/4.5.2.tar.gz')

    # Standard variants
    variant('shared', default=True,
            description='Enables the build of shared libraries')
    variant('lapack', default=False, description='Include Lapack library support')
    variant('powerpc', default=False, description='Enable PowerPC for GCC')
    variant('vsx', default=False, description='Enable POWER8 and above VSX (64-bit little-endian)')
    variant('fast-math', default=False,
            description='Enable -ffast-math (not recommended for GCC 4.6.x)')

    # OpenCV modules
    variant('calib3d', default=False, description='calib3d module')
    variant('core', default=True, description='Include opencv_core module into the OpenCV build')
    variant('cudacodec', default=False, description='Enable video encoding/decoding with CUDA')
    variant('dnn', default=False, description='Build DNN support')
    variant('features2d', default=False, description='features2d module')
    variant('flann', default=False, description='flann module')
    variant('highgui', default=False, description='Include opencv_highgui module into the OpenCV build')
    variant('imgcodecs', default=False, description='Include opencv_imgcodecs module into the OpenCV build')
    variant('imgproc', default=False, description='Include opencv_imgproc module into the OpenCV build')
    variant('java', default=False,
            description='Activates support for Java')
    variant('ml', default=False, description='Build ML support')
    variant('python', default=False,
            description='Enables the build of Python extensions')
    variant('stitching', default=False, description='stitching module')
    variant('superres', default=False, description='superres module')
    variant('ts', default=False, description='Include opencv_ts module into the OpenCV build')
    variant('video', default=False, description='video module')
    variant('videostab', default=False, description='videostab module')
    variant('videoio', default=False, description='videoio module')

    # Optional 3rd party components
    variant('eigen', default=False, description='Activates support for eigen')
    variant('ipp', default=False, description='Activates support for IPP')
    variant('ipp_iw', default=False, description='Build IPP IW from source')
    variant('jasper', default=False, description='Activates support for JasPer')
    variant('jpeg', default=False, description='Include JPEG support')
    variant('opencl', default=False, description='Include OpenCL Runtime support')
    variant('opencl_svm', default=False, description='Include OpenCL Shared Virtual Memory support')
    variant('openclamdfft', default=False, description='Include OpenCL AMD OpenCL FFT library support')
    variant('openclamdblas', default=False, description='Include OpenCL AMD OpenCL BLAS library support')
    variant('openmp', default=False, description='Activates support for OpenMP threads')
    variant('pthreads_pf', default=False, description='Use pthreads-based parallel_for')
    variant('png', default=False, description='Include PNG support')
    variant('qt', default=False, description='Activates support for QT')
    variant('gtk', default=False, description='Activates support for GTK')
    variant('tiff', default=False, description='Include TIFF support')
    variant('vtk', default=False, description='Activates support for VTK')
    variant('zlib', default=False, description='Build zlib from source')

    variant('contrib', default=False, description='Adds in code from opencv_contrib.')
    contrib_vers = [
        '3.4.12', '4.0.0', '4.0.1', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.5.0', '4.5.1'
    ]
    for cv in contrib_vers:
        resource(name="contrib",
                 git='https://github.com/opencv/opencv_contrib.git',
                 tag="{0}".format(cv),
                 when='@{0}+contrib'.format(cv))

    depends_on('hdf5', when='+contrib')
    depends_on('hdf5', when='+cuda')
    depends_on('blas', when='+lapack')

    # Patch to fix conflict between CUDA and OpenCV (reproduced with 3.3.0
    # and 3.4.1) header file that have the same name.Problem is fixed in
    # the current development branch of OpenCV. See #8461 for more information.
    patch('dnn_cuda.patch', when='@3.3.0:3.4.1+cuda+dnn')

    patch('opencv3.2_cmake.patch', when='@3.2')
    patch('opencv3.2_vtk.patch', when='@3.2+vtk')
    patch('opencv3.2_regacyvtk.patch', when='@3.2+vtk')
    patch('opencv3.2_ffmpeg.patch', when='@3.2+videoio')
    patch('opencv3.2_python3.7.patch', when='@3.2+python')
    patch('opencv3.2_fj.patch', when='@3.2 %fj')

    depends_on('eigen', when='+eigen')
    depends_on('zlib', when='+zlib')
    depends_on('libpng', when='+png')
    depends_on('jpeg', when='+jpeg')
    depends_on('libtiff', when='+tiff')

    depends_on('jasper', when='+jasper')
    depends_on('cuda', when='+cuda')
    depends_on('gtkplus', when='+gtk')
    depends_on('vtk', when='+vtk')
    depends_on('qt', when='+qt')
    depends_on('java', when='+java')
    depends_on('ant', when='+java', type='build')
    depends_on('py-numpy', when='+python', type=('build', 'run'))
    depends_on('protobuf@3.5.0:', when='@3.4.1: +dnn')
    depends_on('protobuf@3.1.0', when='@3.3.0:3.4.0 +dnn')

    depends_on('ffmpeg', when='+videoio')
    depends_on('mpi', when='+videoio')

    # TODO For Cuda >= 10, make sure 'dynlink_nvcuvid.h' or 'nvcuvid.h'
    # exists, otherwise build will fail
    # See https://github.com/opencv/opencv_contrib/issues/1786
    conflicts('^cuda@10:', when='+cudacodec')
    conflicts('+cuda', when='~contrib', msg='cuda support requires +contrib')

    # IPP is provided x86_64 only
    conflicts('+ipp', when="arch=aarch64:")

    # Module opencv_calib3d disabled because opencv_flann dependency
    # can't be resolved!
    conflicts('+calib3d', when='~flann')

    extends('python', when='+python')

    def cmake_args(self):
        spec = self.spec

        # Standard variants
        args = [
            '-DBUILD_SHARED_LIBS:BOOL={0}'.format((
                'ON' if '+shared' in spec else 'OFF')),
            '-DENABLE_PRECOMPILED_HEADERS:BOOL=OFF',
            '-DWITH_LAPACK={0}'.format((
                'ON' if '+lapack' in spec else 'OFF')),
            '-DENABLE_POWERPC={0}'.format((
                'ON' if '+powerpc' in spec else 'OFF')),
            '-DENABLE_VSX={0}'.format((
                'ON' if '+vsx' in spec else 'OFF')),
            '-DENABLE_FAST_MATH={0}'.format((
                'ON' if '+fast-math' in spec else 'OFF')),
        ]

        # modules
        args.extend([
            '-DBUILD_opencv_calib3d={0}'.format((
                'ON' if '+calib3d' in spec else 'OFF')),
            '-DBUILD_opencv_core:BOOL={0}'.format((
                'ON' if '+core' in spec else 'OFF')),
            '-DBUILD_opencv_cudacodec={0}'.format((
                'ON' if '+cudacodec' in spec else 'OFF')),
            '-DBUILD_opencv_dnn:BOOL={0}'.format((
                'ON' if '+dnn' in spec else 'OFF')),
            '-DBUILD_opencv_features2d={0}'.format((
                'ON' if '+features2d' in spec else 'OFF')),
            '-DBUILD_opencv_flann={0}'.format((
                'ON' if '+flann' in spec else 'OFF')),
            '-DBUILD_opencv_highgui:BOOL={0}'.format((
                'ON' if '+highgui' in spec else 'OFF')),
            '-DBUILD_opencv_imgcodecs:BOOL={0}'.format((
                'ON' if '+imgcodecs' in spec else 'OFF')),
            '-DBUILD_opencv_imgproc:BOOL={0}'.format((
                'ON' if '+imgproc' in spec else 'OFF')),
            '-DBUILD_opencv_java:BOOL={0}'.format((
                'ON' if '+java' in spec else 'OFF')),
            '-DBUILD_opencv_ml={0}'.format((
                'ON' if '+ml' in spec else 'OFF')),
            '-DBUILD_opencv_stitching={0}'.format((
                'ON' if '+stitching' in spec else 'OFF')),
            '-DBUILD_opencv_superres={0}'.format((
                'ON' if '+superres' in spec else 'OFF')),
            '-DBUILD_opencv_ts={0}'.format((
                'ON' if '+ts' in spec else 'OFF')),
            '-DBUILD_opencv_video={0}'.format((
                'ON' if '+video' in spec else 'OFF')),
            '-DBUILD_opencv_videostab={0}'.format((
                'ON' if '+videostab' in spec else 'OFF')),
            '-DBUILD_opencv_videoio={0}'.format((
                'ON' if '+videoio' in spec else 'OFF')),
        ])

        # 3rd party components
        args.extend([
            '-DBUILD_IPP_IW:BOOL={0}'.format((
                'ON' if '+ipp_iw' in spec else 'OFF')),
            '-DWITH_CUDA:BOOL={0}'.format((
                'ON' if '+cuda' in spec else 'OFF')),
            '-DWITH_EIGEN:BOOL={0}'.format((
                'ON' if '+eigen' in spec else 'OFF')),
            '-DWITH_IPP:BOOL={0}'.format((
                'ON' if '+ipp' in spec else 'OFF')),
            '-DWITH_JASPER:BOOL={0}'.format((
                'ON' if '+jasper' in spec else 'OFF')),
            '-DWITH_JPEG:BOOL={0}'.format((
                'ON' if '+jpeg' in spec else 'OFF')),
            '-DWITH_OPENCL:BOOL={0}'.format((
                'ON' if '+opencl' in spec else 'OFF')),
            '-DWITH_OPENCL_SVM:BOOL={0}'.format((
                'ON' if '+opencl_svm' in spec else 'OFF')),
            '-DWITH_OPENCLAMDFFT:BOOL={0}'.format((
                'ON' if '+openclamdfft' in spec else 'OFF')),
            '-DWITH_OPENCLAMDBLAS:BOOL={0}'.format((
                'ON' if '+openclamdblas' in spec else 'OFF')),
            '-DWITH_OPENMP:BOOL={0}'.format((
                'ON' if '+openmp' in spec else 'OFF')),
            '-DWITH_PTHREADS_PF:BOOL={0}'.format((
                'ON' if '+pthreads_pf' in spec else 'OFF')),
            '-DWITH_PNG:BOOL={0}'.format((
                'ON' if '+png' in spec else 'OFF')),
            '-DWITH_QT:BOOL={0}'.format((
                'ON' if '+qt' in spec else 'OFF')),
            '-DWITH_TIFF:BOOL={0}'.format((
                'ON' if '+tiff' in spec else 'OFF')),
            '-DWITH_VTK:BOOL={0}'.format((
                'ON' if '+vtk' in spec else 'OFF')),
            '-DWITH_PROTOBUF:BOOL={0}'.format((
                'ON' if '@3.3.0: +dnn' in spec else 'OFF')),
            '-DBUILD_PROTOBUF:BOOL=OFF',
            '-DPROTOBUF_UPDATE_FILES={0}'.format('ON')
        ])

        if '+contrib' in spec:
            args.append('-DOPENCV_EXTRA_MODULES_PATH={0}'.format(
                join_path(self.stage.source_path, 'opencv_contrib/modules')))

        if '+cuda' in spec:
            if spec.variants['cuda_arch'].value[0] != 'none':
                cuda_arch = [x for x in spec.variants['cuda_arch'].value if x]
                args.append('-DCUDA_ARCH_BIN={0}'.format(
                    ' '.join(cuda_arch)))

        # Media I/O
        if '+zlib' in spec:
            zlib = spec['zlib']
            args.extend([
                '-DZLIB_LIBRARY_{0}:FILEPATH={1}'.format((
                    'DEBUG' if 'build_type=Debug' in spec else 'RELEASE'),
                    zlib.libs[0]),
                '-DZLIB_INCLUDE_DIR:PATH={0}'.format(
                    zlib.headers.directories[0])
            ])

        if '+png' in spec:
            libpng = spec['libpng']
            args.extend([
                '-DPNG_LIBRARY_{0}:FILEPATH={1}'.format((
                    'DEBUG' if 'build_type=Debug' in spec else 'RELEASE'),
                    libpng.libs[0]),
                '-DPNG_INCLUDE_DIR:PATH={0}'.format(
                    libpng.headers.directories[0])
            ])

        if '+jpeg' in spec:
            libjpeg = spec['jpeg']
            args.extend([
                '-DBUILD_JPEG:BOOL=OFF',
                '-DJPEG_LIBRARY:FILEPATH={0}'.format(libjpeg.libs[0]),
                '-DJPEG_INCLUDE_DIR:PATH={0}'.format(
                    libjpeg.headers.directories[0])
            ])

        if '+tiff' in spec:
            libtiff = spec['libtiff']
            args.extend([
                '-DTIFF_LIBRARY_{0}:FILEPATH={1}'.format((
                    'DEBUG' if 'build_type=Debug' in spec else 'RELEASE'),
                    libtiff.libs[0]),
                '-DTIFF_INCLUDE_DIR:PATH={0}'.format(
                    libtiff.headers.directories[0])
            ])

        if '+jasper' in spec:
            jasper = spec['jasper']
            args.extend([
                '-DJASPER_LIBRARY_{0}:FILEPATH={1}'.format((
                    'DEBUG' if 'build_type=Debug' in spec else 'RELEASE'),
                    jasper.libs[0]),
                '-DJASPER_INCLUDE_DIR:PATH={0}'.format(
                    jasper.headers.directories[0])
            ])

        # GUI
        if '+gtk' not in spec:
            args.extend([
                '-DWITH_GTK:BOOL=OFF',
                '-DWITH_GTK_2_X:BOOL=OFF'
            ])
        elif '^gtkplus@3:' in spec:
            args.extend([
                '-DWITH_GTK:BOOL=ON',
                '-DWITH_GTK_2_X:BOOL=OFF'
            ])
        elif '^gtkplus@2:3' in spec:
            args.extend([
                '-DWITH_GTK:BOOL=OFF',
                '-DWITH_GTK_2_X:BOOL=ON'
            ])

        # Python
        if '+python' in spec:
            python_exe = spec['python'].command.path
            python_lib = spec['python'].libs[0]
            python_include_dir = spec['python'].headers.directories[0]

            if '^python@3:' in spec:
                args.extend([
                    '-DBUILD_opencv_python3=ON',
                    '-DPYTHON3_EXECUTABLE={0}'.format(python_exe),
                    '-DPYTHON3_LIBRARY={0}'.format(python_lib),
                    '-DPYTHON3_INCLUDE_DIR={0}'.format(python_include_dir),
                    '-DBUILD_opencv_python2=OFF',
                ])
            elif '^python@2:3' in spec:
                args.extend([
                    '-DBUILD_opencv_python2=ON',
                    '-DPYTHON2_EXECUTABLE={0}'.format(python_exe),
                    '-DPYTHON2_LIBRARY={0}'.format(python_lib),
                    '-DPYTHON2_INCLUDE_DIR={0}'.format(python_include_dir),
                    '-DBUILD_opencv_python3=OFF',
                ])
        else:
            args.extend([
                '-DBUILD_opencv_python2=OFF',
                '-DBUILD_opencv_python3=OFF'
            ])

        return args

    @property
    def libs(self):
        shared = "+shared" in self.spec
        return find_libraries(
            "libopencv_*", root=self.prefix, shared=shared, recursive=True
        )

# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
class Opencv(CMakePackage, CudaPackage):
    """OpenCV (Open Source Computer Vision Library) is an open source computer
    vision and machine learning software library."""

    homepage = 'https://opencv.org/'
    url      = 'https://github.com/opencv/opencv/archive/4.5.0.tar.gz'
    git      = 'https://github.com/opencv/opencv.git'

    maintainers = ['bvanessen', 'adamjstewart']

    version('master', branch='master')
    version('4.5.2',    sha256='ae258ed50aa039279c3d36afdea5c6ecf762515836b27871a8957c610d0424f8')
    version('4.5.1',    sha256='e27fe5b168918ab60d58d7ace2bd82dd14a4d0bd1d3ae182952c2113f5637513')
    version('4.5.0',    sha256='dde4bf8d6639a5d3fe34d5515eab4a15669ded609a1d622350c7ff20dace1907')
    version('4.2.0',    sha256='9ccb2192d7e8c03c58fee07051364d94ed7599363f3b0dce1c5e6cc11c1bb0ec')
    version('4.1.2',    sha256='385dd0a9c25e67ef0dd60e022d2a2d7b17e2f36819cf3cb46aa8cdff5c5282c9')
    version('4.1.1',    sha256='5de5d96bdfb9dad6e6061d70f47a0a91cee96bb35afb9afb9ecb3d43e243d217')
    version('4.1.0',    sha256='8f6e4ab393d81d72caae6e78bd0fd6956117ec9f006fba55fcdb88caf62989b7')
    version('4.0.1',    sha256='7b86a0ee804244e0c407321f895b15e4a7162e9c5c0d2efc85f1cadec4011af4')
    version('4.0.0',    sha256='3787b3cc7b21bba1441819cb00c636911a846c0392ddf6211d398040a1e4886c')
    version('3.4.12',   sha256='c8919dfb5ead6be67534bf794cb0925534311f1cd5c6680f8164ad1813c88d13')
    version('3.4.6',    sha256='e7d311ff97f376b8ee85112e2b536dbf4bdf1233673500175ed7cf21a0089f6d')
    version('3.4.5',    sha256='0c57d9dd6d30cbffe68a09b03f4bebe773ee44dc8ff5cd6eaeb7f4d5ef3b428e')
    version('3.4.4',    sha256='a35b00a71d77b484f73ec485c65fe56c7a6fa48acd5ce55c197aef2e13c78746')
    version('3.4.3',    sha256='4eef85759d5450b183459ff216b4c0fa43e87a4f6aa92c8af649f89336f002ec')
    version('3.4.1',    sha256='f1b87684d75496a1054405ae3ee0b6573acaf3dad39eaf4f1d66fdd7e03dc852')
    version('3.4.0',    sha256='678cc3d2d1b3464b512b084a8cca1fad7de207c7abdf2caa1fed636c13e916da')
    version('3.3.1',    sha256='5dca3bb0d661af311e25a72b04a7e4c22c47c1aa86eb73e70063cd378a2aa6ee')
    version('3.3.0',    sha256='8bb312b9d9fd17336dc1f8b3ac82f021ca50e2034afc866098866176d985adc6')
    version('3.2.0',    sha256='9541efbf68f298f45914b4e837490647f4d5e472b4c0c04414a787d116a702b2', deprecated=True)
    version('3.1.0',    sha256='f3b160b9213dd17aa15ddd45f6fb06017fe205359dbd1f7219aad59c98899f15', deprecated=True)
    version('2.4.13.2', sha256='4b00c110e6c54943cbbb7cf0d35c5bc148133ab2095ee4aaa0ac0a4f67c58080', deprecated=True)
    version('2.4.13.1', sha256='0d5ce5e0973e3a745f927d1ee097aaf909aae59f787be6d27a03d639e2d96bd7', deprecated=True)
    version('2.4.13',   sha256='94ebcca61c30034d5fb16feab8ec12c8a868f5162d20a9f0396f0f5f6d8bbbff', deprecated=True)
    version('2.4.12.3', sha256='a4cbcd2d470860b0cf1f8faf504619c18a8ac38fd414c5a88ed3e94c963aa750', deprecated=True)
    version('2.4.12.2', sha256='150a165eb14a5ea74fb94dcc16ac7d668a6ff20a4449df2570734a2abaab9c0e', deprecated=True)
    version('2.4.12.1', sha256='c1564771f79304a2597ae4f74f44032021e3a46657e4a117060c08f5ed05ad83', deprecated=True)

    # OpenCV modules (variants)
    # Defined in `modules/*/CMakeLists.txt` using
    # `ocv_add_module(...)` and `ocv_define_module(...)`
    modules = [
        'apps', 'calib3d', 'core', 'dnn', 'features2d', 'flann', 'gapi', 'highgui',
        'imgcodecs', 'imgproc', 'java', 'java_bindings_generator', 'js',
        'js_bindings_generator', 'ml', 'objc', 'objc_bindings_generator', 'objdetect',
        'photo', 'python2', 'python3', 'python_bindings_generator', 'python_tests',
        'stitching', 'ts', 'video', 'videoio', 'world'
    ]

    for mod in modules:
        # At least one of these modules must be enabled to build OpenCV
        variant(mod, default=mod == 'core',
                description='Include opencv_{0} module'.format(mod))

    # Optional 3rd party components (variants)
    # Defined in `CMakeLists.txt` and `modules/gapi/cmake/init.cmake`
    # using `OCV_OPTION(WITH_* ...)`
    components = [
        '1394', 'ade', 'android_mediandk', 'android_native_camera', 'aravis',
        'avfoundation', 'cap_ios', 'carotene', 'clp', 'cpufeatures', 'cublas', 'cuda',
        'cudnn', 'cufft', 'directx', 'dshow', 'eigen', 'ffmpeg', 'freetype', 'gdal',
        'gdcm', 'gphoto2', 'gstreamer', 'gtk', 'gtk_2_x', 'halide', 'hpx',
        'imgcodec_hdr', 'imgcode_pfm', 'imgcodec_pxm', 'imgcodec_sunraster',
        'inf_engine', 'ipp', 'itt', 'jasper', 'jpeg', 'lapack', 'librealsense', 'mfx',
        'msmf', 'msmf_dxva', 'ngraph', 'nvcuvid', 'onnx', 'opencl', 'openclamdblas',
        'openclamdfft', 'opencl_d3d11_nv', 'opencl_svm', 'openexr', 'opengl',
        'openjpeg', 'openmp', 'openni', 'openni2', 'openvx', 'plaidml', 'png',
        'protobuf', 'pthreads_pf', 'pvapi', 'qt', 'quirc', 'tbb', 'tengine', 'tiff',
        'ueye', 'v4l', 'va', 'va_intel', 'vtk', 'vulcan', 'webp', 'win32ui', 'ximea',
        'xine'
    ]

    for component in components:
        variant(component, default=False,
                description='Include {0} support'.format(component))

    # Other (variants)
    variant('shared', default=True,
            description='Enables the build of shared libraries')
    variant('powerpc', default=False, description='Enable PowerPC for GCC')
    variant('fast-math', default=False,
            description='Enable -ffast-math (not recommended for GCC 4.6.x)')
    variant('nonfree', default=False, description='Enable non-free algorithms')

    variant('contrib', default=False, description='Adds in code from opencv_contrib.')
    contrib_vers = [
        '3.1.0', '3.2.0', '3.3.0', '3.3.1', '3.4.0', '3.4.1', '3.4.3', '3.4.4',
        '3.4.5', '3.4.6', '3.4.12', '4.0.0', '4.0.1', '4.1.0', '4.1.1',
        '4.1.2', '4.2.0', '4.5.0', '4.5.1', '4.5.2'
    ]
    for cv in contrib_vers:
        resource(name="contrib",
                 git='https://github.com/opencv/opencv_contrib.git',
                 tag="{0}".format(cv),
                 when='@{0}+contrib'.format(cv))

    # Required (dependencies)
    depends_on('cmake@3.5.1:', type='build')
    depends_on('python@2.7:2.8,3.2:', type='build')
    depends_on('zlib@1.2.3:')

    # OpenCV modules (dependencies)
    depends_on('java', when='+java_bindings_generator')
    depends_on('ant', when='+java_bindings_generator', type='build')
    extends('python', when='+python2')
    depends_on('python@2.7:2.8', when='+python2', type=('build', 'link', 'run'))
    depends_on('py-setuptools', when='+python2', type='build')
    depends_on('py-numpy', when='+python2', type=('build', 'run'))
    extends('python', when='+python3')
    depends_on('python@3.2:', when='+python3', type=('build', 'link', 'run'))
    depends_on('py-setuptools', when='+python3', type='build')
    depends_on('py-numpy', when='+python3', type=('build', 'run'))
    depends_on('ffmpeg', when='+videoio')
    depends_on('mpi', when='+videoio')

    # Optional 3rd party components (dependencies)
    depends_on('clp', when='+clp')
    depends_on('cuda@6.5:', when='+cuda')
    depends_on('cuda@:10.2', when='@4.0:4.2+cuda')
    depends_on('cuda@:9.0', when='@3.3.1:3.4+cuda')
    depends_on('cuda@:8', when='@:3.3.0+cuda')
    depends_on('cudnn', when='+cudnn')
    depends_on('cudnn@:7.6', when='@4.0:4.2+cudnn')
    depends_on('cudnn@:7.3', when='@3.3.1:3.4+cudnn')
    depends_on('cudnn@:6', when='@:3.3.0+cudnn')
    depends_on('eigen', when='+eigen')
    depends_on('ffmpeg', when='+ffmpeg')
    depends_on('freetype', when='+freetype')
    depends_on('gdal', when='+gdal')
    depends_on('gtkplus', when='+gtk')
    depends_on('gtkplus@:2', when='+gtk_2_x')
    depends_on('hpx', when='+hpx')
    depends_on('ipp', when='+ipp')
    depends_on('jasper', when='+jasper')
    depends_on('jpeg', when='+jpeg')
    depends_on('lapack', when='+lapack')
    depends_on('onnx', when='+onnx')
    depends_on('opencl', when='+opencl')
    depends_on('openexr', when='+openexr')
    depends_on('gl', when='+opengl')
    depends_on('openjpeg@2:', when='+openjpeg')
    depends_on('libpng', when='+png')
    depends_on('protobuf@3.5.0:', when='@3.4.1: +protobuf')
    depends_on('protobuf@3.1.0', when='@3.3.0:3.4.0 +protobuf')
    depends_on('qt', when='+qt')
    depends_on('tbb', when='+tbb')
    depends_on('libtiff', when='+tiff')
    depends_on('vtk', when='+vtk')
    depends_on('libwebp', when='+webp')

    # Other (dependencies)
    depends_on('hdf5', when='+contrib')

    # OpenCV modules (conflicts)
    # Defined in `apps/*/CMakeLists.txt` using `ocv_add_application(...)`
    # Different apps require different modules, but no way to control which apps
    # are installed. If +apps is requested, make sure all apps can be built.
    conflicts('+apps', when='~calib3d')
    conflicts('+apps', when='~core')
    conflicts('+apps', when='~dnn')
    conflicts('+apps', when='~features2d')
    conflicts('+apps', when='~highgui')
    conflicts('+apps', when='~imgcodecs')
    conflicts('+apps', when='~imgproc')
    conflicts('+apps', when='~objdetect')
    conflicts('+apps', when='~videoio')
    # Defined in `modules/*/CMakeLists.txt` using
    # `ocv_add_module(...)` and `ocv_define_module(...)`
    # If these required dependencies aren't found, CMake will silently
    # disable the requested module
    conflicts('+calib3d', when='~features2d')
    conflicts('+calib3d', when='~flann')
    conflicts('+calib3d', when='~imgproc')
    conflicts('+dnn', when='~core')
    conflicts('+dnn', when='~imgproc')
    conflicts('+features2d', when='~imgproc')
    conflicts('+flann', when='~core')
    conflicts('+gapi', when='~imgproc')
    conflicts('+highgui', when='~imgcodecs')
    conflicts('+highgui', when='~imgproc')
    conflicts('+imgcodecs', when='~imgproc')
    conflicts('+imgproc', when='~core')
    conflicts('+java', when='~core')
    conflicts('+java', when='~imgproc')
    conflicts('+java', when='~java_bindings_generator')
    conflicts('+js', when='~js_bindings_generator')
    conflicts('+ml', when='~core')
    conflicts('+objc', when='~core')
    conflicts('+objc', when='~imgproc')
    conflicts('+objc', when='~objc_bindings_generator')
    conflicts('+objc_bindings_generator', when='~core')
    conflicts('+objc_bindings_generator', when='~imgproc')
    conflicts('+objdetect', when='~calib3d')
    conflicts('+objdetect', when='~core')
    conflicts('+objdetect', when='~imgproc')
    conflicts('+photo', when='~imgproc')
    conflicts('+python2', when='~python_bindings_generator')
    conflicts('+python2', when='+python3')
    conflicts('+python3', when='~python_bindings_generator')
    conflicts('+python3', when='+python2')
    conflicts('+stitching', when='~calib3d')
    conflicts('+stitching', when='~features2d')
    conflicts('+stitching', when='~flann')
    conflicts('+stitching', when='~imgproc')
    conflicts('+ts', when='~core')
    conflicts('+ts', when='~highgui')
    conflicts('+ts', when='~imgcodecs')
    conflicts('+ts', when='~imgproc')
    conflicts('+ts', when='~videoio')
    conflicts('+video', when='~imgproc')
    conflicts('+videoio', when='~imgcodecs')
    conflicts('+videoio', when='~imgproc')
    conflicts('+world', when='~core')

    # Optional 3rd party components (conflicts)
    # Defined in `CMakeLists.txt` and `modules/gapi/cmake/init.cmake`
    # using `OCV_OPTION(WITH_* ...)`
    conflicts('+ade', when='~gapi')
    conflicts('+android_mediandk', when='platform=darwin', msg='Android only')
    conflicts('+android_mediandk', when='platform=linux', msg='Android only')
    conflicts('+android_mediandk', when='platform=cray', msg='Android only')
    conflicts('+android_native_camera', when='platform=darwin', msg='Android only')
    conflicts('+android_native_camera', when='platform=linux', msg='Android only')
    conflicts('+android_native_camera', when='platform=cray', msg='Android only')
    conflicts('+avfoundation', when='platform=linux', msg='iOS/macOS only')
    conflicts('+avfoundation', when='platform=cray', msg='iOS/macOS only')
    conflicts('+cap_ios', when='platform=darwin', msg='iOS only')
    conflicts('+cap_ios', when='platform=linux', msg='iOS only')
    conflicts('+cap_ios', when='platform=cray', msg='iOS only')
    conflicts('+carotene', when='target=x86:', msg='ARM/AARCH64 only')
    conflicts('+carotene', when='target=x86_64:', msg='ARM/AARCH64 only')
    conflicts('+cpufeatures', when='platform=darwin', msg='Android only')
    conflicts('+cpufeatures', when='platform=linux', msg='Android only')
    conflicts('+cpufeatures', when='platform=cray', msg='Android only')
    conflicts('+cublas', when='~cuda')
    conflicts('+cudnn', when='~cuda')
    conflicts('+cufft', when='~cuda')
    conflicts('+directx', when='platform=darwin', msg='Windows only')
    conflicts('+directx', when='platform=linux', msg='Windows only')
    conflicts('+directx', when='platform=cray', msg='Windows only')
    conflicts('+dshow', when='platform=darwin', msg='Windows only')
    conflicts('+dshow', when='platform=linux', msg='Windows only')
    conflicts('+dshow', when='platform=cray', msg='Windows only')
    conflicts('+freetype', when='~gapi')
    conflicts('+gtk', when='platform=darwin', msg='Linux only')
    conflicts('+gtk_2_x', when='platform=darwin', msg='Linux only')
    conflicts('+ipp', when='target=aarch64:', msg='x86 or x86_64 only')
    conflicts('+msmf', when='platform=darwin', msg='Windows only')
    conflicts('+msmf', when='platform=linux', msg='Windows only')
    conflicts('+msmf', when='platform=cray', msg='Windows only')
    conflicts('+msmf_dxva', when='platform=darwin', msg='Windows only')
    conflicts('+msmf_dxva', when='platform=linux', msg='Windows only')
    conflicts('+msmf_dxva', when='platform=cray', msg='Windows only')
    conflicts('+nvcuvid', when='~cuda')
    conflicts('+opencl_d3d11_nv', when='platform=darwin', msg='Windows only')
    conflicts('+opencl_d3d11_nv', when='platform=linux', msg='Windows only')
    conflicts('+opencl_d3d11_nv', when='platform=cray', msg='Windows only')
    conflicts('+plaidml', when='~gapi')
    conflicts('+tengine', when='platform=darwin', msg='Linux only')
    conflicts('+tengine', when='target=x86:', msg='ARM/AARCH64 only')
    conflicts('+tengine', when='target=x86_64:', msg='ARM/AARCH64 only')
    conflicts('+ueye', when='platform=darwin', msg='Linux only')
    conflicts('+v4l', when='platform=darwin', msg='Linux only')
    conflicts('+va', when='platform=darwin', msg='Linux only')
    conflicts('+va_intel', when='platform=darwin', msg='Linux only')
    conflicts('+win32ui', when='platform=darwin', msg='Windows only')
    conflicts('+win32ui', when='platform=linux', msg='Windows only')
    conflicts('+win32ui', when='platform=cray', msg='Windows only')
    conflicts('+xine', when='platform=darwin', msg='Linux only')

    # Other (conflicts)
    conflicts('+cuda', when='~contrib', msg='cuda support requires +contrib')

    # Patch to fix conflict between CUDA and OpenCV (reproduced with 3.3.0
    # and 3.4.1) header file that have the same name. Problem is fixed in
    # the current development branch of OpenCV. See #8461 for more information.
    patch('dnn_cuda.patch', when='@3.3.0:3.4.1+cuda+dnn')

    patch('opencv3.2_cmake.patch', when='@3.2:3.4.1')
    patch('opencv3.2_compiler_cmake.patch', when='@3.2')
    patch('opencv3.2_vtk.patch', when='@3.2+vtk')
    patch('opencv3.2_regacyvtk.patch', when='@3.2+vtk')
    patch('opencv3.2_ffmpeg.patch', when='@3.2+videoio')
    patch('opencv3.2_python3.7.patch', when='@3.2+python3')
    patch('opencv3.2_fj.patch', when='@3.2 %fj')

    def cmake_args(self):
        spec = self.spec
        args = []

        # OpenCV modules
        for mod in self.modules:
            args.append(self.define_from_variant('BUILD_opencv_' + mod, mod))

        # Optional 3rd party components
        for component in self.components:
            args.append(self.define_from_variant(
                'WITH_' + component.upper(), component))

        # Other
        args.extend([
            self.define('ENABLE_CONFIG_VERIFICATION', True),
            self.define_from_variant('BUILD_SHARED_LIBS', 'shared'),
            self.define('ENABLE_PRECOMPILED_HEADERS', False),
            self.define_from_variant('WITH_LAPACK', 'lapack'),
            self.define_from_variant('ENABLE_POWERPC', 'powerpc'),
            self.define_from_variant('ENABLE_FAST_MATH', 'fast-math'),
            self.define_from_variant('OPENCV_ENABLE_NONFREE', 'nonfree'),
        ])

        if '+contrib' in spec:
            args.append(self.define('OPENCV_EXTRA_MODULES_PATH', join_path(
                self.stage.source_path, 'opencv_contrib/modules')))

        if '+cuda' in spec:
            if spec.variants['cuda_arch'].value[0] != 'none':
                cuda_arch = spec.variants['cuda_arch'].value
                args.append(self.define('CUDA_ARCH_BIN', ' '.join(cuda_arch)))

        # TODO: this CMake flag is deprecated
        if spec.target.family == 'ppc64le':
            args.append(self.define('ENABLE_VSX', True))

        # Media I/O
        zlib = spec['zlib']
        args.extend([
            self.define('BUILD_ZLIB', False),
            self.define('ZLIB_LIBRARY', zlib.libs[0]),
            self.define('ZLIB_INCLUDE_DIR', zlib.headers.directories[0]),
        ])

        if '+png' in spec:
            libpng = spec['libpng']
            args.extend([
                self.define('BUILD_PNG', False),
                self.define('PNG_LIBRARY', libpng.libs[0]),
                self.define('PNG_INCLUDE_DIR', libpng.headers.directories[0])
            ])

        if '+jpeg' in spec:
            libjpeg = spec['jpeg']
            args.extend([
                self.define('BUILD_JPEG', False),
                self.define('JPEG_LIBRARY', libjpeg.libs[0]),
                self.define('JPEG_INCLUDE_DIR', libjpeg.headers.directories[0])
            ])

        if '+tiff' in spec:
            libtiff = spec['libtiff']
            args.extend([
                self.define('BUILD_TIFF', False),
                self.define('TIFF_LIBRARY', libtiff.libs[0]),
                self.define('TIFF_INCLUDE_DIR', libtiff.headers.directories[0])
            ])

        if '+jasper' in spec:
            jasper = spec['jasper']
            args.extend([
                self.define('BUILD_JASPER', False),
                self.define('JASPER_LIBRARY', jasper.libs[0]),
                self.define('JASPER_INCLUDE_DIR', jasper.headers.directories[0])
            ])

        # Python
        python_exe = spec['python'].command.path
        python_lib = spec['python'].libs[0]
        python_include_dir = spec['python'].headers.directories[0]

        if '+python2' in spec:
            args.extend([
                self.define('PYTHON2_EXECUTABLE', python_exe),
                self.define('PYTHON2_LIBRARY', python_lib),
                self.define('PYTHON2_INCLUDE_DIR', python_include_dir),
                self.define('PYTHON3_EXECUTABLE', '')
            ])
        elif '+python3' in spec:
            args.extend([
                self.define('PYTHON3_EXECUTABLE', python_exe),
                self.define('PYTHON3_LIBRARY', python_lib),
                self.define('PYTHON3_INCLUDE_DIR', python_include_dir),
                self.define('PYTHON2_EXECUTABLE', '')
            ])
        else:
            args.extend([
                self.define('PYTHON2_EXECUTABLE', ''),
                self.define('PYTHON3_EXECUTABLE', ''),
            ])

        return args

    @property
    def libs(self):
        shared = '+shared' in self.spec
        return find_libraries(
            'libopencv_*', root=self.prefix, shared=shared, recursive=True
        )

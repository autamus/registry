# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ants(CMakePackage):
    """ANTs extracts information from complex datasets that include imaging.
       Paired with ANTsR (answer), ANTs is useful for managing, interpreting
       and visualizing multidimensional data. ANTs is popularly considered a
       state-of-the-art medical image registration and segmentation toolkit.
       ANTs depends on the Insight ToolKit (ITK), a widely used medical image
       processing library to which ANTs developers contribute.
    """

    homepage = "https://stnava.github.io/ANTs/"
    url      = "https://github.com/ANTsX/ANTs/archive/v2.2.0.tar.gz"

    version('2.3.5', sha256='2fddfd5f274a47f1c383e734a7e763b627c4a8383d2d3b9971561f335016bb0a')
    version('2.2.0', sha256='62f8f9ae141cb45025f4bb59277c053acf658d4a3ba868c9e0f609af72e66b4a')

    depends_on('zlib', type='link')

    variant('minc', default=True, description='Build ITK with MINC support')

    def cmake_args(self):
        return [
            self.define_from_variant('ITK_BUILD_MINC_SUPPORT', 'minc')
        ]

    def install(self, spec, prefix):
        with working_dir(
                join_path(self.build_directory, 'ANTS-build'),
                create=False
        ):
            make("install")
        install_tree('Scripts', prefix.bin)

    def setup_run_environment(self, env):
        env.set('ANTSPATH', self.prefix.bin)

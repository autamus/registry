# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class UniversalCtags(AutotoolsPackage):
    """Universal Ctags generates an index (or tag) file of language
    objects found in source files for many popular programming languages.
    This index makes it easy for text editors and other tools to locate
    the indexed items."""

    homepage = "https://ctags.io/"
    url      = "https://github.com/universal-ctags/ctags/archive/p5.9.20220102.0.tar.gz"
    git      = "https://github.com/universal-ctags/ctags.git"

    version('master', branch='master')
    version('5.9.20220102.0', sha256='0f795d1d38ac46de843c2b7297f1cfaca72014ba1d5b88d11bd578d869c475bb')
    version('5.9.20211114.0', sha256='7f5e1dc3a6955eace0d57dcc1194ada32188f984a71d46e1d98e029fbd559f86')
    version('5.9.20210912.0', sha256='5082d4f7e5695be3d697c46e2232d76c6d8adff51d22ba7a4b869362f444ee21')
    version('5.9.20210808.0', sha256='7f5f88d20750dfa2437ca9d163972b8684e3cf16de022a5177f322be92f528cc')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('libiconv', type='link')
    depends_on('pkgconfig', type='build')

    def autoreconf(self, spec, prefix):
        which('bash')('autogen.sh')

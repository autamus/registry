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
    url      = "https://github.com/universal-ctags/ctags/archive/p5.9.20211017.0.tar.gz"
    git      = "https://github.com/universal-ctags/ctags.git"

    version('master', branch='master')
    version('5.9.20211017.0', sha256='a755ddb11b6635a1e0ca64ce9b647d8a567f04b59da03ebd548e7ef07c699ad3')
    version('5.9.20210912.0', sha256='5082d4f7e5695be3d697c46e2232d76c6d8adff51d22ba7a4b869362f444ee21')
    version('5.9.20210808.0', sha256='7f5f88d20750dfa2437ca9d163972b8684e3cf16de022a5177f322be92f528cc')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('libiconv', type='link')
    depends_on('pkg-config', type='build')

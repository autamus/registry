# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mothur(MakefilePackage):
    """This project seeks to develop a single piece of open-source, expandable
       software to fill the bioinformatics needs of the microbial ecology
       community."""

    homepage = "https://github.com/mothur/mothur"
    url      = "https://github.com/mothur/mothur/archive/v1.45.1.tar.gz"

    version('1.45.1', sha256='5e568f03cabb35adc53b053ee62ef8c4b3198b33bf6933144b9568aba38af6ff', url='https://github.com/mothur/mothur/archive/v1.45.1.tar.gz')
    version('1.45.0', sha256='b22e1b4ba8686f4e77e6a55a30a1a1cb6490b651398b0756d84f80314f55aa70', url='https://github.com/mothur/mothur/archive/v.1.45.0.tar.gz')
    version('1.44.3', sha256='a9825ccbb7f60b527f63c16e07f9dd45373bdc8ee65c8f2f0b45f8b2113b2e6f', url='https://github.com/mothur/mothur/archive/v1.44.3.tar.gz')
    version('1.43.0', sha256='12ccd95a85bec3bb1564b8feabd244ea85413973740754803d01fc71ecb0a2c1')
    version('1.42.1', sha256='6b61591dda289ac2d8361f9c1547ffbeeba3b9fbdff877dd286bad850bbd5539')
    version('1.40.5', sha256='a0fbdfa68b966d7adc4560e3787506a0dad8b47b4b996c2663cd6c0b416d101a')
    version('1.39.5', sha256='9f1cd691e9631a2ab7647b19eb59cd21ea643f29b22cde73d7f343372dfee342')

    variant('vsearch', default=False,  description='Use vsearch')

    depends_on('boost')
    depends_on('readline')
    depends_on('vsearch@2.13.3',  when='+vsearch', type='run')

    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')
        makefile.filter('BOOST_LIBRARY_DIR=\"\\\"Enter_your_boost_library_path'
                        '_here\\\"\"', 'BOOST_LIBRARY_DIR=%s' %
                        self.spec['boost'].prefix.lib)
        makefile.filter('BOOST_INCLUDE_DIR=\"\\\"Enter_your_boost_include_path'
                        '_here\\\"\"', 'BOOST_INCLUDE_DIR=%s' %
                        self.spec['boost'].prefix.include)
        makefile.filter('MOTHUR_FILES=\"\\\"Enter_your_default_path_'
                        'here\\\"\"', 'MOTHUR_FILES=%s' % prefix)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('mothur', prefix.bin)
        install('uchime', prefix.bin)
        install_tree('source', prefix.include)


# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Stringtie(MakefilePackage):
    """StringTie is a fast and highly efficient assembler of RNA-Seq alignments
       into potential transcripts."""

    homepage = "https://ccb.jhu.edu/software/stringtie"
    url      = "https://github.com/gpertea/stringtie/archive/v2.1.7.tar.gz"

    version('2.1.7', sha256='a58b7b5395f059713894daa2f31d6b4aa8ad17c25398821d5d4ab601b6314b79', url='https://github.com/gpertea/stringtie/archive/v2.1.7.tar.gz')
    version('2.1.6', sha256='5045520de5871debe008fa599d63e760efc585568288c7d1852ffc8444335f18', url='https://github.com/gpertea/stringtie/archive/v2.1.6.tar.gz')
    version('2.1.5', sha256='6e1b3f758aebc567cbfcc3b6cc53f197049323457e1d445957ca6b29035d6aaa', url='https://github.com/gpertea/stringtie/archive/v2.1.5.tar.gz')
    version('1.3.4', sha256='0134c0adc264efd31a1df4301b33bfcf3b3fe96bd3990ce3df90819bad9af968')
    version('1.3.3', sha256='30e8a3a29b474f0abeef1540d9b4624a827d8b29d7347226d86a38afea28bc0f')

    depends_on('samtools')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('stringtie', prefix.bin)

# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Stringtie(MakefilePackage):
    """StringTie is a fast and highly efficient assembler of RNA-Seq alignments
       into potential transcripts."""

    homepage = "https://ccb.jhu.edu/software/stringtie"
    url      = "https://github.com/gpertea/stringtie/archive/v2.2.0.tar.gz"

    version('2.2.0', sha256='ef000db642aaa0c4bb1a88017f25becb5dd87b48d7fc2534640d2f73bbc5ec52')
    version('1.3.4', sha256='0134c0adc264efd31a1df4301b33bfcf3b3fe96bd3990ce3df90819bad9af968')
    version('1.3.3', sha256='30e8a3a29b474f0abeef1540d9b4624a827d8b29d7347226d86a38afea28bc0f')

    depends_on('samtools')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('stringtie', prefix.bin)

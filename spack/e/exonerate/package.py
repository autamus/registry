# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Exonerate(AutotoolsPackage):
    """Pairwise sequence alignment of DNA and proteins"""

    homepage = "http://www.ebi.ac.uk/about/vertebrate-genomics/software/exonerate"
    url      = "http://ftp.ebi.ac.uk/pub/software/vertebrategenomics/exonerate/exonerate-2.4.0.tar.gz"

    version('2.4.0', sha256='f849261dc7c97ef1f15f222e955b0d3daf994ec13c9db7766f1ac7e77baa4042')

    depends_on('pkgconfig', type="build")
    depends_on('glib')

    parallel = False

    def configure_args(self):
        args = []

        args.append('--disable-debug')
        args.append('--disable-dependency-tracking')

        return args

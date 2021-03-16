# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Tophat(AutotoolsPackage):
    """Spliced read mapper for RNA-Seq."""

    homepage = "http://ccb.jhu.edu/software/tophat/index.shtml"
    url      = "https://github.com/infphilo/tophat/archive/v2.1.1.tar.gz"

    version('2.1.2', sha256='15016b82255dad085d4ee7d970e50f0e53a280d466335553d47790d8344ff4b1')
    version('2.1.1', sha256='991b1b7c840a5f5c4e9a15b2815983257d2b0748246af0b9094c7d07552b023e')

    depends_on('autoconf', type='build')
    # 2.1.1 only builds with automake@1.15.1.  There's a patch here:
    # https://github.com/spack/spack/pull/8244, which was incorporated
    # upstream in 2.1.2, which is known to build with 1.16.1 and 1.15.1.
    depends_on('automake',                        type='build')
    depends_on('automake@1.15.1', when='@:2.1.1', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('boost@1.47:')
    depends_on('bowtie2', type='run')

    parallel = False

    def configure_args(self):
        return ["--with-boost={0}".format(self.spec['boost'].prefix)]

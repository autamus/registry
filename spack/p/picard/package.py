# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import glob
import os.path
import re


class Picard(Package):
    """Picard is a set of command line tools for manipulating high-throughput
       sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF.
    """

    homepage = "http://broadinstitute.github.io/picard/"
    url      = "https://github.com/broadinstitute/picard/releases/download/2.25.0/picard.jar"
    _urlfmt  = "https://github.com/broadinstitute/picard/releases/download/{0}/picard.jar"
    _oldurlfmt = 'https://github.com/broadinstitute/picard/releases/download/{0}/picard-tools-{0}.zip'

    # They started distributing a single jar file at v2.6.0, prior to
    # that it was a .zip file with multiple .jar and .so files
    version('2.25.0', sha256='faf2434da84fe21b516d57817767920fdedfc19ebdc01d9cae8d6d3314f7e897', url='https://github.com/broadinstitute/picard/releases/download/2.25.0/picard.jar')
    version('2.24.0', sha256='70e91039bccc6f6db60f18c41713218a8cdf45f591f02c1012c062152b27cd7b')
    version('2.20.8', sha256='aff92d618ee9e6bafc1ab4fbfa89fc557a0dbe596ae4b92fe3bf93ebf95c7105')
    version('2.19.0', sha256='f97fc3f7a73b55cceea8b6a6488efcf1b2fbf8cad61d88645704ddd45a8c5950')
    version('2.18.3', sha256='0e0fc45d9a822ee9fa562b3bb8f1525a439e4cd541429a1a4ca4646f37189b70')
    version('2.18.0', sha256='c4c64b39ab47968e4afcaf1a30223445ee5082eab31a03eee240e54c2e9e1dce')
    version('2.17.0', sha256='ffea8bf90e850919c0833e9dcc16847d40090a1ef733c583a710a3282b925998')
    version('2.16.0', sha256='01cf3c930d2b4841960497491512d327bf669c1ed2e753152e1e651a27288c2d')
    version('2.15.0', sha256='dc3ff74c704954a10796b390738078617bb0b0fef15731e9d268ed3b26c6a285')
    version('2.13.2', sha256='db7749f649e8423053fb971e6af5fb8a9a1a797cb1f20fef1100edf9f82f6f94')
    version('2.10.0', sha256='e256d5e43656b7d8be454201a7056dce543fe9cbeb30329a0d8c22d28e655775')
    version('2.9.4', sha256='0ecee9272bd289d902cc18053010f0364d1696e7518ac92419a99b2f0a1cf689')
    version('2.9.3', sha256='6cca26ce5094b25a82e1a8d646920d584c6db5f009476196dc285be6522e00ce')
    version('2.9.2', sha256='05714b9743a7685a43c94a93f5d03aa4070d3ab6e20151801301916d3e546eb7')
    version('2.9.0', sha256='9a57f6bd9086ea0f5f1a6d9d819459854cb883bb8093795c916538ed9dd5de64')
    version('2.8.3', sha256='97a4b6c8927c8cb5f3450630c9b39bf210ced8c271f198119118ce1c24b8b0f6')
    version('2.6.0', sha256='671d9e86e6bf0c28ee007aea55d07e2456ae3a57016491b50aab0fd2fd0e493b')
    version('1.140', sha256='0d27287217413db6b846284c617d502eaa578662dcb054a7017083eab9c54438')
        if version < Version('2.6.0'):
            return self._oldurlfmt.format(version)
        else:
            return self._urlfmt.format(version)

# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Nrm(PythonPackage):
    """Node Resource Manager"""

    homepage = "https://xgitlab.cels.anl.gov/argo/nrm"
    url = "https://www.mcs.anl.gov/research/projects/argo/downloads/nrm-0.1.0.tar.gz"
    version('0.1.0', sha256='911a848042fa50ed216c818e0667bcd3e4219687eb5a35476b7313abe12106dc')

    depends_on('py-setuptools', type=('build'))

    depends_on('py-six', type=('build', 'run'))
    depends_on('py-pyzmq@17.1.2', type=('build', 'run'))
    depends_on('py-pyyaml', type=('build', 'run'))
    depends_on('py-tornado@5.1.1', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-argparse@1.2.1:', type=('build', 'run'), when='^python@:2.6')
    depends_on('py-jsonschema@2.6.0', type=('build', 'run'))
    depends_on('py-warlock', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))

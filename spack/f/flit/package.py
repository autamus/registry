# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Flit(MakefilePackage):
    """Floating-point Litmus Tests (FLiT) is a C++ test infrastructure for
    detecting variability in floating-point code caused by variations in
    compiler code generation, hardware and execution environments."""

    homepage = "https://pruners.github.io/flit"
    url      = "https://github.com/PRUNERS/FLiT"
    url      = "https://github.com/PRUNERS/FLiT/archive/v2.1.0.tar.gz"

    tags = ['e4s']

    version('2.1.0', sha256='b31ffa02fda1ab0f5555acdc6edc353d93d53ae8ef85e099f83bcf1c83e70885')

    maintainers = ['mikebentley15']

    # Add dependencies
    depends_on('python@3:',      type='run')
    depends_on('py-toml',        type='run')
    depends_on('py-pyelftools',  type='run')
    depends_on('gmake',          type=('run', 'build'))
    depends_on('sqlite@3:',      type='run')

    def edit(self, spec, prefix):
        env['PREFIX'] = prefix

# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Restic(Package):
    """Fast, secure, efficient backup program."""

    homepage = "https://restic.net"
    url      = "https://github.com/restic/restic/releases/download/v0.13.0/restic-0.13.0.tar.gz"

    maintainers = ['alecbcs']

    version('0.13.0', sha256='b3c09137b462548f44d764f98909534bef6e85fe029d4daf60545642cdefd3dd')
    version('0.12.1', sha256='a9c88d5288ce04a6cc78afcda7590d3124966dab3daa9908de9b3e492e2925fb')

    depends_on("go", type='build')

    def setup_build_environment(self, env):
        # Point GOPATH at the top of the staging dir for the build step.
        env.prepend_path('GOPATH', self.stage.path)

    def install(self, spec, prefix):
        go('run', 'build.go')
        mkdirp(prefix.bin)
        install('restic', prefix.bin)

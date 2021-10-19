# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Beast2(Package):
    """BEAST is a cross-platform program for Bayesian inference using MCMC
       of molecular sequences. It is entirely orientated towards rooted,
       time-measured phylogenies inferred using strict or relaxed molecular
       clock models. It can be used as a method of reconstructing phylogenies
       but is also a framework for testing evolutionary hypotheses without
       conditioning on a single tree topology."""

    homepage = "http://beast2.org/"
    url      = "https://github.com/CompEvol/beast2/releases/download/v2.6.4/BEAST.v2.6.4.Linux.tgz"

    version('2.6.4', sha256='4f80e2920eb9d87f3e9f64433119774dc67aca390fbd13dd480f852e3f8701a4')
    version('2.6.3', sha256='8899277b0d7124ab04dc512444d45f0f1a13505f3ce641e1f117098be3e2e20d')
    version('2.5.2', sha256='2feb2281b4f7cf8f7de1a62de50f52a8678ed0767fc72f2322e77dde9b8cd45f')
    version('2.4.6', sha256='84029c5680cc22f95bef644824130090f5f12d3d7f48d45cb4efc8e1d6b75e93')

    depends_on('java')

    def setup_run_environment(self, env):
        env.set('BEAST', self.prefix)

    def install(self, spec, prefix):
        install_tree('bin', prefix.bin)
        install_tree('examples', join_path(self.prefix, 'examples'))
        install_tree('images', join_path(self.prefix, 'images'))
        install_tree('lib', prefix.lib)
        install_tree('templates', join_path(self.prefix, 'templates'))

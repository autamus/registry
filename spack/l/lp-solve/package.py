# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class LpSolve(Package):
    """lp_solve is a Mixed Integer Linear Programming (MILP) solver."""

    homepage = "https://sourceforge.net/projects/lpsolve/"
    url      = "https://sourceforge.net/projects/lpsolve/files/lpsolve/5.5.2.9/lp_solve_5.5.2.9_source.tar.gz"

    version('5.5.2.11', sha256='6d4abff5cc6aaa933ae8e6c17a226df0fc0b671c438f69715d41d09fe81f902f')
    version('5.5.2.9', sha256='67cd78b6dc78d63b43dd4bcc1214b829af03f7f7c11265795b516f8b4807686a', url='https://sourceforge.net/projects/lpsolve/files/lpsolve/5.5.2.9/lp_solve_5.5.2.9_source.tar.gz')

    def install(self, spec, prefix):
        with working_dir('lpsolve55'):
            mkdir(prefix.lib)
            sh = which('sh')
            sh('-x', 'ccc')
            install_tree('bin/ux64', prefix.lib)
        with working_dir('lp_solve'):
            mkdir(prefix.bin)
            sh = which('sh')
            sh('-x', 'ccc')
            install_tree('bin/ux64', prefix.bin)

        mkdirp(prefix.include.lpsolve)
        headers = find('.', '*.h', recursive=False)
        for header in headers:
            install(header, prefix.include.lpsolve)

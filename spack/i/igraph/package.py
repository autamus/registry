# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Igraph(AutotoolsPackage):
    """igraph is a library for creating and manipulating graphs."""

    homepage = "http://igraph.org/"
    url      = "https://github.com/igraph/igraph/releases/download/0.9.4/igraph-0.9.4.tar.gz"

    version('0.9.4', sha256='a3285cccf4f043c9ced2bc8d8d2609ff8398cb92ed49fdf86264ed91929137dd', url='https://github.com/igraph/igraph/releases/download/0.9.4/igraph-0.9.4.tar.gz')
    version('0.7.1', sha256='d978030e27369bf698f3816ab70aa9141e9baf81c56cc4f55efbe5489b46b0df')

    depends_on('automake', type='build')
    depends_on('autoconf', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4')

    depends_on('libxml2')

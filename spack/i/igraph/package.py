# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Igraph(AutotoolsPackage):
    """igraph is a library for creating and manipulating graphs."""

    homepage = "https://igraph.org/"
    url      = "https://github.com/igraph/igraph/releases/download/0.9.9/igraph-0.9.9.tar.gz"

    version('0.9.9', sha256='ee358d9bd13e3b491533e3eda5cda934bc5238aa756a68c2defaab4e33ee57ab')
    version('0.7.1', sha256='d978030e27369bf698f3816ab70aa9141e9baf81c56cc4f55efbe5489b46b0df')

    depends_on('libxml2')

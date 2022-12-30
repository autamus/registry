# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Igraph(AutotoolsPackage):
    """igraph is a library for creating and manipulating graphs."""

    homepage = "https://igraph.org/"
    url      = "https://github.com/igraph/igraph/releases/download/0.10.3/igraph-0.10.3.tar.gz"

    version('0.10.3', sha256='5f72398c7847bb167f85159b7a9fe1fe69ce0f241c5de5d30b2b347f9dc3f7c6')
    version('0.7.1', sha256="d978030e27369bf698f3816ab70aa9141e9baf81c56cc4f55efbe5489b46b0df")

    depends_on("libxml2")

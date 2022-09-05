# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Igraph(AutotoolsPackage):
    """igraph is a library for creating and manipulating graphs."""

    homepage = "https://igraph.org/"
    url      = "https://github.com/igraph/igraph/releases/download/0.10.0/igraph-0.10.0.tar.gz"

    version('0.10.0', sha256='62e3c9e51ac5b0f1871142aac23956f3a6a337fee980bf5474bd4ac3d76e1a68')
    version('0.7.1', sha256="d978030e27369bf698f3816ab70aa9141e9baf81c56cc4f55efbe5489b46b0df")

    depends_on("libxml2")

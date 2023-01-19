# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from llnl.util import tty

import spack.build_systems.cmake
import spack.build_systems.generic
from spack.package import *


class Superlu(CMakePackage, Package):
    """SuperLU is a general purpose library for the direct solution of large,
    sparse, nonsymmetric systems of linear equations on high performance
    machines. SuperLU is designed for sequential machines."""

    homepage = "https://crd-legacy.lbl.gov/~xiaoye/SuperLU/#superlu"
    url      = "https://github.com/xiaoyeli/superlu/archive/refs/tags/v5.3.0.tar.gz"

    tags = ["e4s"]

    version('5.3.0', sha256="3e464afa77335de200aeb739074a11e96d9bef6d0b519950cfa6684c4be1f350")
    version('5.2.2', sha256="470334a72ba637578e34057f46948495e601a5988a602604f5576367e606a28c")
    version('5.2.1', sha256="28fb66d6107ee66248d5cf508c79de03d0621852a0ddeba7301801d3d859f463")
    version('4.3', sha256="169920322eb9b9c6a334674231479d04df72440257c17870aaa0139d74416781", url='https://crd-legacy.lbl.gov/~xiaoye/SuperLU/superlu_4.3.tar.gz')
    version('4.2', sha256="5a06e19bf5a597405dfeea39fe92aa8c5dd41da73c72c7187755a75f581efb28", url='https://crd-legacy.lbl.gov/~xiaoye/SuperLU/superlu_4.2.tar.gz')

    build_system(
        conditional("cmake", when="@5:"), conditional("autotools", when="@:4"), default="cmake"
    )

    variant("pic", default=True, description="Build with position independent code")

    depends_on("blas")
    conflicts(
        "@:5.2.1",
        when="%apple-clang@12:",
        msg="Older SuperLU is incompatible with newer compilers",
    )

    test_requires_compiler = True

    # Pre-cmake installation method
    examples_src_dir = "EXAMPLE"
    make_hdr_file = "make.inc"

    @run_after("install")
    def cache_test_sources(self):
        """Copy the example source files after the package is installed to an
        install test subdirectory for use during `spack test run`."""
        if self.spec.satisfies("@5.2.2:"):
            # Include dir was hardcoded in 5.2.2
            filter_file(
                r"INCLUDEDIR  = -I\.\./SRC",
                "INCLUDEDIR = -I" + self.prefix.include,
                join_path(self.examples_src_dir, "Makefile"),
            )

        self.cache_extra_test_sources(self.examples_src_dir)

    def _generate_make_hdr_for_test(self):
        config_args = []

        # Define make.inc file
        config_args.extend(
            [
                "SuperLUroot = {0}".format(self.prefix),
                "SUPERLULIB = {0}/libsuperlu.a".format(self.prefix.lib),
                "BLASLIB    = {0}".format(self.spec["blas"].libs.ld_flags),
                "TMGLIB     = libtmglib.a",
                "LIBS       = $(SUPERLULIB) $(BLASLIB)",
                "ARCH       = ar",
                "ARCHFLAGS  = cr",
                "RANLIB     = {0}".format("ranlib" if which("ranlib") else "echo"),
                "CC         = {0}".format(env["CC"]),
                "FORTRAN    = {0}".format(env["FC"]),
                "LOADER     = {0}".format(env["CC"]),
                "CFLAGS     = -O3 -DNDEBUG -DUSE_VENDOR_BLAS -DPRNTlevel=0 -DAdd_",
                "NOOPTS     = -O0",
            ]
        )

        return config_args

    # Pre-cmake configuration
    @when("@:4")
    def _generate_make_hdr_for_test(self):
        config_args = []

        # Define make.inc file
        config_args.extend(
            [
                "PLAT       = _x86_64",
                "SuperLUroot = {0}".format(self.prefix),
                "SUPERLULIB = {0}/libsuperlu_{1}.a".format(self.prefix.lib, self.spec.version),
                "BLASLIB    = {0}".format(self.spec["blas"].libs.ld_flags),
                "TMGLIB     = libtmglib.a",
                "LIBS       = $(SUPERLULIB) $(BLASLIB)",
                "ARCH       = ar",
                "ARCHFLAGS  = cr",
                "RANLIB     = {0}".format("ranlib" if which("ranlib") else "echo"),
                "CC         = {0}".format(env["CC"]),
                "FORTRAN    = {0}".format(env["FC"]),
                "LOADER     = {0}".format(env["CC"]),
                "CFLAGS     = -O3 -DNDEBUG -DUSE_VENDOR_BLAS -DPRNTlevel=0 -DAdd_",
                "NOOPTS     = -O0",
            ]
        )

        return config_args

    def run_superlu_test(self, test_dir, exe, args):
        if not self.run_test(
            "make",
            options=args,
            purpose="test: compile {0} example".format(exe),
            work_dir=test_dir,
        ):
            tty.warn("Skipping test: failed to compile example")
            return

        if not self.run_test(exe, purpose="test: run {0} example".format(exe), work_dir=test_dir):
            tty.warn("Skipping test: failed to run example")

    def test(self):
        config_args = self._generate_make_hdr_for_test()

        # Write configuration options to make.inc file
        make_file_inc = join_path(self.test_suite.current_test_cache_dir, self.make_hdr_file)
        with open(make_file_inc, "w") as inc:
            for option in config_args:
                inc.write("{0}\n".format(option))

        args = []
        if self.version < Version("5.2.2"):
            args.append("HEADER=" + self.prefix.include)
        args.append("superlu")

        test_dir = join_path(self.test_suite.current_test_cache_dir, self.examples_src_dir)
        exe = "superlu"

        if not os.path.isfile(join_path(test_dir, "{0}.c".format(exe))):
            tty.warn("Skipping superlu test:" "missing file {0}.c".format(exe))
            return

        self.run_superlu_test(test_dir, exe, args)


class CMakeBuilder(spack.build_systems.cmake.CMakeBuilder):
    def cmake_args(self):
        if self.pkg.version > Version("5.2.1"):
            _blaslib_key = "enable_internal_blaslib"
        else:
            _blaslib_key = "enable_blaslib"
        args = [
            self.define(_blaslib_key, False),
            self.define("CMAKE_INSTALL_LIBDIR", self.prefix.lib),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
            self.define("enable_tests", self.pkg.run_tests),
        ]
        return args


class GenericBuilder(spack.build_systems.generic.GenericBuilder):
    def install(self, pkg, spec, prefix):
        """Use autotools before version 5"""
        # Define make.inc file
        config = [
            "PLAT       = _x86_64",
            "SuperLUroot = %s" % self.pkg.stage.source_path,
            # 'SUPERLULIB = $(SuperLUroot)/lib/libsuperlu$(PLAT).a',
            "SUPERLULIB = $(SuperLUroot)/lib/libsuperlu_{0}.a".format(self.pkg.spec.version),
            "BLASDEF    = -DUSE_VENDOR_BLAS",
            "BLASLIB    = {0}".format(spec["blas"].libs.ld_flags),
            # or BLASLIB      = -L/usr/lib64 -lblas
            "TMGLIB     = libtmglib.a",
            "LIBS       = $(SUPERLULIB) $(BLASLIB)",
            "ARCH       = ar",
            "ARCHFLAGS  = cr",
            "RANLIB     = {0}".format("ranlib" if which("ranlib") else "echo"),
            "CC         = {0}".format(env["CC"]),
            "FORTRAN    = {0}".format(env["FC"]),
            "LOADER     = {0}".format(env["CC"]),
            "CDEFS      = -DAdd_",
        ]

        if "+pic" in spec:
            config.extend(
                [
                    # Use these lines instead when pic_flag capability arrives
                    "CFLAGS     = -O3 {0}".format(self.pkg.compiler.cc_pic_flag),
                    "NOOPTS     = {0}".format(self.pkg.compiler.cc_pic_flag),
                    "FFLAGS     = -O2 {0}".format(self.pkg.compiler.f77_pic_flag),
                    "LOADOPTS   = {0}".format(self.pkg.compiler.cc_pic_flag),
                ]
            )
        else:
            config.extend(
                ["CFLAGS     = -O3", "NOOPTS     = ", "FFLAGS     = -O2", "LOADOPTS   = "]
            )

        with open("make.inc", "w") as inc:
            for option in config:
                inc.write("{0}\n".format(option))

        make(parallel=False)

        install_tree("lib", prefix.lib)
        mkdir(prefix.include)
        install(join_path("SRC", "*.h"), prefix.include)

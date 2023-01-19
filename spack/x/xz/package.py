# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack.package import *


class Xz(AutotoolsPackage, SourceforgePackage):
    """XZ Utils is free general-purpose data compression software with
    high compression ratio. XZ Utils were written for POSIX-like systems,
    but also work on some not-so-POSIX systems. XZ Utils are the successor
    to LZMA Utils."""

    homepage = "https://tukaani.org/xz/"
    sourceforge_mirror_path = "lzmautils/files/xz-5.2.5.tar.bz2"
    list_url = "https://tukaani.org/xz/old.html"

    executables = [r"^xz$"]

    version('5.2.7', sha256="b65f1d0c2708e57716f4dd2216989a73847ac6fdb4168ffceb155767e22b834b")
    version('5.2.6', sha256="13e3402e301b6018f6a71ef0e497f714c6d11e214ae82dab156b81c2a64acb25")
    version('5.2.5', sha256="5117f930900b341493827d63aa910ff5e011e0b994197c3b71c08a20228a42df")
    version('5.2.4', sha256="3313fd2a95f43d88e44264e6b015e7d03053e681860b0d5d3f9baca79c57b7bf")
    version('5.2.3', sha256="fd9ca16de1052aac899ad3495ad20dfa906c27b4a5070102a2ec35ca3a4740c1")
    version('5.2.2', sha256="6ff5f57a4b9167155e35e6da8b529de69270efb2b4cf3fbabf41a4ee793840b5")
    version('5.2.1', sha256="679148f497e0bff2c1adce42dee5a23f746e71321c33ebb0f641a302e30c2a80")
    version('5.2.0', sha256="f7357d7455a1670229b3cca021da71dd5d13b789db62743c20624bdffc9cc4a5")

    variant("pic", default=False, description="Compile with position independent code.")

    variant(
        "libs",
        default="shared,static",
        values=("shared", "static"),
        multi=True,
        description="Build shared libs, static libs or both",
    )

    # xz-5.2.7/src/liblzma/common/common.h:56 uses attribute __symver__ instead of
    # __asm__(.symver) for newer GCC releases.
    conflicts("%intel", when="@5.2.7", msg="icc does not support attribute __symver__")

    def configure_args(self):
        return self.enable_or_disable("libs")

    def flag_handler(self, name, flags):
        if name == "cflags" and "+pic" in self.spec:
            flags.append(self.compiler.cc_pic_flag)
        return (flags, None, None)

    @property
    def libs(self):
        return find_libraries(["liblzma"], root=self.prefix, recursive=True)

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"xz \(XZ Utils\) (\S+)", output)
        return match.group(1) if match else None

    @run_after("install")
    def darwin_fix(self):
        if self.spec.satisfies("platform=darwin"):
            fix_darwin_install_name(self.prefix.lib)

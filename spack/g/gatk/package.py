# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os.path


class Gatk(Package):
    """
    Genome Analysis Toolkit
    Variant Discovery in High-Throughput Sequencing Data
    """

    homepage = "https://software.broadinstitute.org/gatk/"
    url      = "https://github.com/broadinstitute/gatk/releases/download/4.2.0.0/gatk-4.2.0.0.zip"
    list_url = "https://github.com/broadinstitute/gatk/releases"
    version('N/A', sha256="42e6de5059232df1ad5785c68c39a53dc1b54afe7bb086d0129f4dc95fb182bc")
    version('4.2.0.0', sha256='dd11cc8e3bc7a23c2c226366428f0908c902765eabbc1c641c736c06b80aaf78', url='https://github.com/broadinstitute/gatk/releases/download/4.2.0.0/gatk-4.2.0.0.zip')

    depends_on("java@8", type="run")
    depends_on("python@2.6:2.8,3.6:", type="run", when="@4.0:")
    depends_on("r@3.2:", type="run", when="@4.0:")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)

        # For ver 3.x will install "GenomeAnalysisTK.jar"
        # For ver 4.x will install both "gatk-package-<ver>-local.jar"
        # and "gatk-package-<ver>-spark.jar"
        install("*.jar", prefix.bin)

        # Skip helper script for versions >4.0
        if spec.satisfies("@4.0:"):
            install("gatk", prefix.bin)
        else:
            # Set up a helper script to call java on the jar file,
            # explicitly codes the path for java and the jar file.
            script_sh = join_path(os.path.dirname(__file__), "gatk.sh")
            script = join_path(prefix.bin, "gatk")
            install(script_sh, script)
            set_executable(script)

            # Munge the helper script to explicitly point to java and the
            # jar file.
            java = join_path(self.spec["java"].prefix, "bin", "java")
            kwargs = {"ignore_absent": False, "backup": False, "string": False}
            filter_file("^java", java, script, **kwargs)
            filter_file(
                "GenomeAnalysisTK.jar",
                join_path(prefix.bin, "GenomeAnalysisTK.jar"),
                script,
                **kwargs
            )

    def setup_run_environment(self, env):
        env.prepend_path(
            "GATK", join_path(self.prefix.bin, "GenomeAnalysisTK.jar")
        )

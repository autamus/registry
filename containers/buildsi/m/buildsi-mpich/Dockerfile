FROM spack/ubuntu-bionic:latest

RUN spack install --source mpich@3.4.1 \
&&  spack install --source mpich@3.3.2 \
&&  spack install --source mpich@3.1.4 device=ch3 netmod=tcp \
&&  spack install --source mpich@3.0.4 device=ch3 netmod=tcp

ENV PACKAGE_VERSIONS="3.4.1 3.3.2 3.1.4 3.0.4"

FROM spack/ubuntu-bionic:latest

RUN spack install mpich@3.4.1 \
&&  spack install mpich@3.4 \
&&  spack install mpich@3.3.2 \
&&  spack install mpich@3.3.1 \
&&  spack install mpich@3.2 device=ch3 \
&&  spack install mpich@3.1.4 device=ch3 netmod=tcp \
&&  spack install mpich@3.1.3 device=ch3 netmod=tcp \
&&  spack install mpich@3.1.1 device=ch3 netmod=tcp \
&&  spack install mpich@3.1 device=ch3 netmod=tcp \
&&  spack install mpich@3.0.4 device=ch3 netmod=tcp

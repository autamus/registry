FROM spack/ubuntu-bionic:latest as base

RUN mkdir /opt/spack-environment \
&&  (echo "spack:" \
&&   echo "  specs:" \
&&   echo "  - mpich@3.4.1" \
&&   echo "  - mpich@3.4" \
&&   echo "  - mpich@3.3.2" \
&&   echo "  - mpich@3.3.1" \
&&   echo "  - mpich@3.2" \
&&   echo "  - mpich@3.1.4" \
&&   echo "  - mpich@3.1.3" \
&&   echo "  - mpich@3.1.1" \
&&   echo "  - mpich@3.1" \
&&   echo "  - mpich@3.0.4" \
&&   echo "  config:" \
&&   echo "    install_tree: /opt/software" \
&&   echo "  view: /opt/view") > /opt/spack-environment/spack.yaml

# Install the software, remove unnecessary deps
RUN cd /opt/spack-environment && spack env activate . && spack install --fail-fast && spack gc -y

# Modifications to the environment that are necessary to run
RUN cd /opt/spack-environment && \
    spack env activate --sh -d . >> /etc/profile.d/z10_spack_environment.sh

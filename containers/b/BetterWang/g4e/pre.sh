#!/bin/bash

# Adding the EIC Spack Repository
git clone https://github.com/eic/eic-spack.git /opt/eic-spack

# Add this repository to your Spack configuration
spack repo add /opt/eic-spack

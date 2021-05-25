---
layout: container
name: psi4
github: https://github.com/autamus/registry/blob/main/containers/p/psi4/spack.yaml
versions:
- 1.3.2
updated_at: 2021-05-25T13:46:18.93067361Z
size: 175MB
description: Psi4 is an open-source suite of ab initio quantum chemistry programs
  designed for efficient, high-accuracy simulations of a variety of molecular properties.
container_url: https://github.com/orgs/autamus/packages/container/package/psi4

---
# psi4
```bash 
Download        : docker pull ghcr.io/autamus/psi4
Compressed Size : 175MB
```

## Description
Psi4 is an open-source suite of ab initio quantum chemistry programs designed for efficient, high-accuracy simulations of a variety of molecular properties.

## Usage
### Pull (Download)
To download the latest version of psi4 run,

```bash
docker pull ghcr.io/autamus/psi4:latest
```

or to download a specific version of psi4 run,

```bash
docker pull ghcr.io/autamus/psi4:1.3.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/psi4 psi4 --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/psi4 bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the psi4 container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/psi4 psi4 /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC psi4 container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-psi4/).
---
layout: container
name: plasma
github: https://github.com/autamus/registry/blob/main/containers/p/plasma/spack.yaml
versions:
- 20.9.20
- 21.8.29
- 22.9.29
updated_at: 2022-11-05T22:06:31.745205924Z
size: 52MB
description: Parallel Linear Algebra Software for Multicore Architectures, PLASMA
  is a software package for solving problems in dense linear algebra using multicore
  processors and Xeon Phi coprocessors. PLASMA provides implementations of state-of-the-art
  algorithms using cutting-edge task scheduling techniques. PLASMA currently offers
  a collection of routines for solving linear systems of equations, least squares
  problems, eigenvalue problems, and singular value problems.
container_url: https://github.com/orgs/autamus/packages/container/package/plasma

---
# plasma
```bash 
Download        : docker pull ghcr.io/autamus/plasma
Compressed Size : 52MB
```

## Description
Parallel Linear Algebra Software for Multicore Architectures, PLASMA is a software package for solving problems in dense linear algebra using multicore processors and Xeon Phi coprocessors. PLASMA provides implementations of state-of-the-art algorithms using cutting-edge task scheduling techniques. PLASMA currently offers a collection of routines for solving linear systems of equations, least squares problems, eigenvalue problems, and singular value problems.

## Usage
### Pull (Download)
To download the latest version of plasma run,

```bash
docker pull ghcr.io/autamus/plasma:latest
```

or to download a specific version of plasma run,

```bash
docker pull ghcr.io/autamus/plasma:20.9.20
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/plasma plasma --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/plasma bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the plasma container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/plasma plasma /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC plasma container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-plasma/).
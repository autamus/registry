---
layout: container
name: gcc
github: https://github.com/autamus/registry/blob/main/containers/g/gcc/spack.yaml
versions:
- 11.1.0
updated_at: 2021-05-25T17:28:33.052489084Z
size: 106MB
description: The GNU Compiler Collection includes front ends for C, C++, Objective-C,
  Fortran, Ada, and Go, as well as libraries for these languages.
container_url: https://github.com/orgs/autamus/packages/container/package/gcc

---
# gcc
```bash 
Download        : docker pull ghcr.io/autamus/gcc
Compressed Size : 106MB
```

## Description
The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, and Go, as well as libraries for these languages.

## Usage
### Pull (Download)
To download the latest version of gcc run,

```bash
docker pull ghcr.io/autamus/gcc:latest
```

or to download a specific version of gcc run,

```bash
docker pull ghcr.io/autamus/gcc:11.1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/gcc gcc --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/gcc bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the gcc container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/gcc gcc /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluser. Check out the SHPC gcc container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-gcc/).
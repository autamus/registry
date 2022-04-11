---
layout: container
name: gmp
github: https://github.com/autamus/registry/blob/main/containers/g/gmp/spack.yaml
versions:
- 6.2.1
updated_at: 2022-04-11T17:07:39.155485651Z
size: 27MB
description: GMP is a free library for arbitrary precision arithmetic, operating on
  signed integers, rational numbers, and floating-point numbers.
container_url: https://github.com/orgs/autamus/packages/container/package/gmp

---
# gmp
```bash 
Download        : docker pull ghcr.io/autamus/gmp
Compressed Size : 27MB
```

## Description
GMP is a free library for arbitrary precision arithmetic, operating on signed integers, rational numbers, and floating-point numbers.

## Usage
### Pull (Download)
To download the latest version of gmp run,

```bash
docker pull ghcr.io/autamus/gmp:latest
```

or to download a specific version of gmp run,

```bash
docker pull ghcr.io/autamus/gmp:6.2.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/gmp gmp --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/gmp bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the gmp container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/gmp gmp /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC gmp container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-gmp/).
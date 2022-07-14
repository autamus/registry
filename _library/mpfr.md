---
layout: container
name: mpfr
github: https://github.com/autamus/registry/blob/main/containers/m/mpfr/spack.yaml
versions:
- 4.1.0
updated_at: 2022-07-14T17:07:27.265248165Z
size: 30MB
description: The MPFR library is a C library for multiple-precision floating-point
  computations with correct rounding.
container_url: https://github.com/orgs/autamus/packages/container/package/mpfr

---
# mpfr
```bash 
Download        : docker pull ghcr.io/autamus/mpfr
Compressed Size : 30MB
```

## Description
The MPFR library is a C library for multiple-precision floating-point computations with correct rounding.

## Usage
### Pull (Download)
To download the latest version of mpfr run,

```bash
docker pull ghcr.io/autamus/mpfr:latest
```

or to download a specific version of mpfr run,

```bash
docker pull ghcr.io/autamus/mpfr:4.1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/mpfr mpfr --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/mpfr bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the mpfr container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/mpfr mpfr /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC mpfr container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-mpfr/).
---
layout: container
name: gsl
github: https://github.com/autamus/registry/blob/main/containers/g/gsl/spack.yaml
versions:
- "2.6"
- "2.7"
updated_at: 2022-01-15T15:52:46.595712504Z
size: 29MB
description: The GNU Scientific Library (GSL) is a numerical library for C and C++
  programmers. It is free software under the GNU General Public License. The library
  provides a wide range of mathematical routines such as random number generators,
  special functions and least-squares fitting. There are over 1000 functions in total
  with an extensive test suite.
container_url: https://github.com/orgs/autamus/packages/container/package/gsl

---
# gsl
```bash 
Download        : docker pull ghcr.io/autamus/gsl
Compressed Size : 29MB
```

## Description
The GNU Scientific Library (GSL) is a numerical library for C and C++ programmers. It is free software under the GNU General Public License. The library provides a wide range of mathematical routines such as random number generators, special functions and least-squares fitting. There are over 1000 functions in total with an extensive test suite.

## Usage
### Pull (Download)
To download the latest version of gsl run,

```bash
docker pull ghcr.io/autamus/gsl:latest
```

or to download a specific version of gsl run,

```bash
docker pull ghcr.io/autamus/gsl:2.6
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/gsl gsl --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/gsl bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the gsl container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/gsl gsl /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC gsl container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-gsl/).
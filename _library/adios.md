---
layout: container
name: adios
github: https://github.com/autamus/registry/blob/main/containers/a/adios/spack.yaml
versions:
- 1.13.1
updated_at: 2022-11-02T21:36:42.742537224Z
size: 71MB
description: 'The Adaptable IO System (ADIOS) provides a simple, flexible way for
  scientists to describe the data in their code that may need to be written, read,
  or processed outside of the running simulation. '
container_url: https://github.com/orgs/autamus/packages/container/package/adios

---
# adios
```bash 
Download        : docker pull ghcr.io/autamus/adios
Compressed Size : 71MB
```

## Description
The Adaptable IO System (ADIOS) provides a simple, flexible way for scientists to describe the data in their code that may need to be written, read, or processed outside of the running simulation. 

## Usage
### Pull (Download)
To download the latest version of adios run,

```bash
docker pull ghcr.io/autamus/adios:latest
```

or to download a specific version of adios run,

```bash
docker pull ghcr.io/autamus/adios:1.13.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/adios adios --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/adios bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the adios container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/adios adios /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC adios container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-adios/).
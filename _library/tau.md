---
layout: container
name: tau
github: https://github.com/autamus/registry/blob/main/containers/t/tau/spack.yaml
versions:
- 2.30.1
updated_at: 2021-10-19T08:00:30.795203185Z
size: 157MB
description: 'A portable profiling and tracing toolkit for performance analysis of
  parallel programs written in Fortran, C, C++, UPC, Java, Python. '
container_url: https://github.com/orgs/autamus/packages/container/package/tau

---
# tau
```bash 
Download        : docker pull ghcr.io/autamus/tau
Compressed Size : 157MB
```

## Description
A portable profiling and tracing toolkit for performance analysis of parallel programs written in Fortran, C, C++, UPC, Java, Python. 

## Usage
### Pull (Download)
To download the latest version of tau run,

```bash
docker pull ghcr.io/autamus/tau:latest
```

or to download a specific version of tau run,

```bash
docker pull ghcr.io/autamus/tau:2.30.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/tau tau --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/tau bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the tau container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/tau tau /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC tau container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-tau/).
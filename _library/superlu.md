---
layout: container
name: superlu
github: https://github.com/autamus/registry/blob/main/containers/s/superlu/spack.yaml
versions:
- 5.2.2
- 5.3.0
updated_at: 2021-10-25T16:47:51.428620942Z
size: 51MB
description: SuperLU is a general purpose library for the direct solution of large,
  sparse, nonsymmetric systems of linear equations on high performance machines. SuperLU
  is designed for sequential machines.
container_url: https://github.com/orgs/autamus/packages/container/package/superlu

---
# superlu
```bash 
Download        : docker pull ghcr.io/autamus/superlu
Compressed Size : 51MB
```

## Description
SuperLU is a general purpose library for the direct solution of large, sparse, nonsymmetric systems of linear equations on high performance machines. SuperLU is designed for sequential machines.

## Usage
### Pull (Download)
To download the latest version of superlu run,

```bash
docker pull ghcr.io/autamus/superlu:latest
```

or to download a specific version of superlu run,

```bash
docker pull ghcr.io/autamus/superlu:5.2.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/superlu superlu --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/superlu bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the superlu container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/superlu superlu /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC superlu container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-superlu/).
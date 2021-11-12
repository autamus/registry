---
layout: container
name: mpich
github: https://github.com/autamus/registry/blob/main/containers/m/mpich/spack.yaml
versions:
- 3.4.2
updated_at: 2021-11-12T04:32:47.453119847Z
size: 49MB
description: MPICH is a high performance and widely portable implementation of the
  Message Passing Interface (MPI) standard.
container_url: https://github.com/orgs/autamus/packages/container/package/mpich

---
# mpich
```bash 
Download        : docker pull ghcr.io/autamus/mpich
Compressed Size : 49MB
```

## Description
MPICH is a high performance and widely portable implementation of the Message Passing Interface (MPI) standard.

## Usage
### Pull (Download)
To download the latest version of mpich run,

```bash
docker pull ghcr.io/autamus/mpich:latest
```

or to download a specific version of mpich run,

```bash
docker pull ghcr.io/autamus/mpich:3.4.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/mpich mpich --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/mpich bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the mpich container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/mpich mpich /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC mpich container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-mpich/).
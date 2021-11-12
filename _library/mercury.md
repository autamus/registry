---
layout: container
name: mercury
github: https://github.com/autamus/registry/blob/main/containers/m/mercury/spack.yaml
versions:
- 2.0.1
updated_at: 2021-11-12T16:06:31.355359107Z
size: 49MB
description: Mercury is a C library for implementing RPC, optimized for HPC
container_url: https://github.com/orgs/autamus/packages/container/package/mercury

---
# mercury
```bash 
Download        : docker pull ghcr.io/autamus/mercury
Compressed Size : 49MB
```

## Description
Mercury is a C library for implementing RPC, optimized for HPC

## Usage
### Pull (Download)
To download the latest version of mercury run,

```bash
docker pull ghcr.io/autamus/mercury:latest
```

or to download a specific version of mercury run,

```bash
docker pull ghcr.io/autamus/mercury:2.0.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/mercury mercury --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/mercury bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the mercury container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/mercury mercury /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC mercury container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-mercury/).
---
layout: container
name: loki
github: https://github.com/autamus/registry/blob/main/containers/l/loki/spack.yaml
versions:
- 0.1.7
updated_at: 2022-05-29T18:34:39.712712575Z
size: 27MB
description: Loki is a C++ library of designs, containing flexible implementations
  of common design patterns and idioms.
container_url: https://github.com/orgs/autamus/packages/container/package/loki

---
# loki
```bash 
Download        : docker pull ghcr.io/autamus/loki
Compressed Size : 27MB
```

## Description
Loki is a C++ library of designs, containing flexible implementations of common design patterns and idioms.

## Usage
### Pull (Download)
To download the latest version of loki run,

```bash
docker pull ghcr.io/autamus/loki:latest
```

or to download a specific version of loki run,

```bash
docker pull ghcr.io/autamus/loki:0.1.7
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/loki loki --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/loki bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the loki container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/loki loki /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC loki container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-loki/).
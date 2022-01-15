---
layout: container
name: astral
github: https://github.com/autamus/registry/blob/main/containers/a/astral/spack.yaml
versions:
- 5.6.1
- 5.7.1
updated_at: 2022-01-15T15:45:31.218723753Z
size: 220MB
description: ASTRAL is a tool for estimating an unrooted species tree given a set
  of unrooted gene trees.
container_url: https://github.com/orgs/autamus/packages/container/package/astral

---
# astral
```bash 
Download        : docker pull ghcr.io/autamus/astral
Compressed Size : 220MB
```

## Description
ASTRAL is a tool for estimating an unrooted species tree given a set of unrooted gene trees.

## Usage
### Pull (Download)
To download the latest version of astral run,

```bash
docker pull ghcr.io/autamus/astral:latest
```

or to download a specific version of astral run,

```bash
docker pull ghcr.io/autamus/astral:5.6.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/astral astral --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/astral bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the astral container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/astral astral /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC astral container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-astral/).
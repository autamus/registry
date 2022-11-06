---
layout: container
name: xnnpack
github: https://github.com/autamus/registry/blob/main/containers/x/xnnpack/spack.yaml
versions:
- 2021.02.22
- 2022.02.16
updated_at: 2022-11-06T21:18:28.580380965Z
size: 27MB
description: High-efficiency floating-point neural network inference operators for
  mobile, server, and Web
container_url: https://github.com/orgs/autamus/packages/container/package/xnnpack

---
# xnnpack
```bash 
Download        : docker pull ghcr.io/autamus/xnnpack
Compressed Size : 27MB
```

## Description
High-efficiency floating-point neural network inference operators for mobile, server, and Web

## Usage
### Pull (Download)
To download the latest version of xnnpack run,

```bash
docker pull ghcr.io/autamus/xnnpack:latest
```

or to download a specific version of xnnpack run,

```bash
docker pull ghcr.io/autamus/xnnpack:2021.02.22
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/xnnpack xnnpack --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/xnnpack bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the xnnpack container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/xnnpack xnnpack /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC xnnpack container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-xnnpack/).
---
layout: container
name: xz
github: https://github.com/autamus/registry/blob/main/containers/x/xz/spack.yaml
versions:
- 5.2.5
updated_at: 2022-05-29T19:51:04.727850261Z
size: 27MB
description: XZ Utils is free general-purpose data compression software with high
  compression ratio. XZ Utils were written for POSIX-like systems, but also work on
  some not-so-POSIX systems. XZ Utils are the successor to LZMA Utils.
container_url: https://github.com/orgs/autamus/packages/container/package/xz

---
# xz
```bash 
Download        : docker pull ghcr.io/autamus/xz
Compressed Size : 27MB
```

## Description
XZ Utils is free general-purpose data compression software with high compression ratio. XZ Utils were written for POSIX-like systems, but also work on some not-so-POSIX systems. XZ Utils are the successor to LZMA Utils.

## Usage
### Pull (Download)
To download the latest version of xz run,

```bash
docker pull ghcr.io/autamus/xz:latest
```

or to download a specific version of xz run,

```bash
docker pull ghcr.io/autamus/xz:5.2.5
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/xz xz --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/xz bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the xz container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/xz xz /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC xz container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-xz/).
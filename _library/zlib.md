---
layout: container
name: zlib
github: https://github.com/autamus/registry/blob/main/containers/z/zlib/spack.yaml
versions:
- 1.2.11
- 1.2.12
- 1.2.13
updated_at: 2022-10-27T18:49:47.461204622Z
size: 27MB
description: 'A free, general-purpose, legally unencumbered lossless data-compression
  library. '
container_url: https://github.com/orgs/autamus/packages/container/package/zlib

---
# zlib
```bash 
Download        : docker pull ghcr.io/autamus/zlib
Compressed Size : 27MB
```

## Description
A free, general-purpose, legally unencumbered lossless data-compression library. 

## Usage
### Pull (Download)
To download the latest version of zlib run,

```bash
docker pull ghcr.io/autamus/zlib:latest
```

or to download a specific version of zlib run,

```bash
docker pull ghcr.io/autamus/zlib:1.2.11
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/zlib zlib --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/zlib bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the zlib container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/zlib zlib /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC zlib container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-zlib/).
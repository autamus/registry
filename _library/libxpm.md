---
layout: container
name: libxpm
github: https://github.com/autamus/registry/blob/main/containers/l/libxpm/spack.yaml
versions:
- 3.5.12
updated_at: 2022-08-01T19:22:12.465712937Z
size: 47MB
description: libXpm - X Pixmap (XPM) image file format library.
container_url: https://github.com/orgs/autamus/packages/container/package/libxpm

---
# libxpm
```bash 
Download        : docker pull ghcr.io/autamus/libxpm
Compressed Size : 47MB
```

## Description
libXpm - X Pixmap (XPM) image file format library.

## Usage
### Pull (Download)
To download the latest version of libxpm run,

```bash
docker pull ghcr.io/autamus/libxpm:latest
```

or to download a specific version of libxpm run,

```bash
docker pull ghcr.io/autamus/libxpm:3.5.12
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/libxpm libxpm --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/libxpm bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the libxpm container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/libxpm libxpm /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC libxpm container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-libxpm/).
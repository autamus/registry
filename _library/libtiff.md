---
layout: container
name: libtiff
github: https://github.com/autamus/registry/blob/main/containers/l/libtiff/spack.yaml
versions:
- 4.1.0
- 4.2.0
- 4.3.0
updated_at: 2022-05-26T15:11:30.569478595Z
size: 27MB
description: LibTIFF - Tag Image File Format (TIFF) Library and Utilities.
container_url: https://github.com/orgs/autamus/packages/container/package/libtiff

---
# libtiff
```bash 
Download        : docker pull ghcr.io/autamus/libtiff
Compressed Size : 27MB
```

## Description
LibTIFF - Tag Image File Format (TIFF) Library and Utilities.

## Usage
### Pull (Download)
To download the latest version of libtiff run,

```bash
docker pull ghcr.io/autamus/libtiff:latest
```

or to download a specific version of libtiff run,

```bash
docker pull ghcr.io/autamus/libtiff:4.1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/libtiff libtiff --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/libtiff bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the libtiff container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/libtiff libtiff /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC libtiff container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-libtiff/).
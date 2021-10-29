---
layout: container
name: libquo
github: https://github.com/autamus/registry/blob/main/containers/l/libquo/spack.yaml
versions:
- 1.3.1
updated_at: 2021-10-29T15:03:45.061732786Z
size: 52MB
description: QUO (as in "status
container_url: https://github.com/orgs/autamus/packages/container/package/libquo

---
# libquo
```bash 
Download        : docker pull ghcr.io/autamus/libquo
Compressed Size : 52MB
```

## Description
QUO (as in "status

## Usage
### Pull (Download)
To download the latest version of libquo run,

```bash
docker pull ghcr.io/autamus/libquo:latest
```

or to download a specific version of libquo run,

```bash
docker pull ghcr.io/autamus/libquo:1.3.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/libquo libquo --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/libquo bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the libquo container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/libquo libquo /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC libquo container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-libquo/).
---
layout: container
name: xrootd
github: https://github.com/autamus/registry/blob/main/containers/x/xrootd/spack.yaml
versions:
- 5.1.0
- 5.3.1
updated_at: 2021-10-25T16:50:44.926767066Z
size: 44MB
description: The XROOTD project aims at giving high performance, scalable fault tolerant
  access to data repositories of many kinds.
container_url: https://github.com/orgs/autamus/packages/container/package/xrootd

---
# xrootd
```bash 
Download        : docker pull ghcr.io/autamus/xrootd
Compressed Size : 44MB
```

## Description
The XROOTD project aims at giving high performance, scalable fault tolerant access to data repositories of many kinds.

## Usage
### Pull (Download)
To download the latest version of xrootd run,

```bash
docker pull ghcr.io/autamus/xrootd:latest
```

or to download a specific version of xrootd run,

```bash
docker pull ghcr.io/autamus/xrootd:5.1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/xrootd xrootd --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/xrootd bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the xrootd container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/xrootd xrootd /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC xrootd container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-xrootd/).
---
layout: container
name: htslib
github: https://github.com/autamus/registry/blob/main/containers/h/htslib/spack.yaml
versions:
- "1.12"
- "1.13"
- "1.14"
updated_at: 2021-10-22T16:58:01.244469182Z
size: 34MB
description: C library for high-throughput sequencing data formats.
container_url: https://github.com/orgs/autamus/packages/container/package/htslib

---
# htslib
```bash 
Download        : docker pull ghcr.io/autamus/htslib
Compressed Size : 34MB
```

## Description
C library for high-throughput sequencing data formats.

## Usage
### Pull (Download)
To download the latest version of htslib run,

```bash
docker pull ghcr.io/autamus/htslib:latest
```

or to download a specific version of htslib run,

```bash
docker pull ghcr.io/autamus/htslib:1.12
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/htslib htslib --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/htslib bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the htslib container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/htslib htslib /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC htslib container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-htslib/).
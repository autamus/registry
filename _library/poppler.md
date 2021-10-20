---
layout: container
name: poppler
github: https://github.com/autamus/registry/blob/main/containers/p/poppler/spack.yaml
versions:
- 0.90.1
- 21.07.0
- 21.08.0
- 21.09.0
- 21.10.0
updated_at: 2021-10-20T03:34:49.520177337Z
size: 77MB
description: Poppler is a PDF rendering library based on the xpdf-3.0 code base.
container_url: https://github.com/orgs/autamus/packages/container/package/poppler

---
# poppler
```bash 
Download        : docker pull ghcr.io/autamus/poppler
Compressed Size : 77MB
```

## Description
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

## Usage
### Pull (Download)
To download the latest version of poppler run,

```bash
docker pull ghcr.io/autamus/poppler:latest
```

or to download a specific version of poppler run,

```bash
docker pull ghcr.io/autamus/poppler:0.90.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/poppler poppler --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/poppler bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the poppler container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/poppler poppler /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC poppler container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-poppler/).
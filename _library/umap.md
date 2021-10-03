---
layout: container
name: umap
github: https://github.com/autamus/registry/blob/main/containers/u/umap/spack.yaml
versions:
- 2.1.0
updated_at: 2021-10-03T22:08:27.325732018Z
size: 27MB
description: Umap is a library that provides an mmap()-like interface to a simple,
  user-space page fault handler based on the userfaultfd Linux feature (starting with
  4.3 linux kernel).
container_url: https://github.com/orgs/autamus/packages/container/package/umap

---
# umap
```bash 
Download        : docker pull ghcr.io/autamus/umap
Compressed Size : 27MB
```

## Description
Umap is a library that provides an mmap()-like interface to a simple, user-space page fault handler based on the userfaultfd Linux feature (starting with 4.3 linux kernel).

## Usage
### Pull (Download)
To download the latest version of umap run,

```bash
docker pull ghcr.io/autamus/umap:latest
```

or to download a specific version of umap run,

```bash
docker pull ghcr.io/autamus/umap:2.1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/umap umap --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/umap bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the umap container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/umap umap /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC umap container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-umap/).
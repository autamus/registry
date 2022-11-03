---
layout: container
name: amrex
github: https://github.com/autamus/registry/blob/main/containers/a/amrex/spack.yaml
versions:
- "21.06"
- "21.07"
- "21.08"
- "21.09"
- "21.10"
- "21.11"
- "22.01"
- "22.11"
updated_at: 2022-11-03T20:18:39.590911764Z
size: 66MB
description: AMReX is a publicly available software framework designed for building
  massively parallel block- structured adaptive mesh refinement (AMR) applications.
container_url: https://github.com/orgs/autamus/packages/container/package/amrex

---
# amrex
```bash 
Download        : docker pull ghcr.io/autamus/amrex
Compressed Size : 66MB
```

## Description
AMReX is a publicly available software framework designed for building massively parallel block- structured adaptive mesh refinement (AMR) applications.

## Usage
### Pull (Download)
To download the latest version of amrex run,

```bash
docker pull ghcr.io/autamus/amrex:latest
```

or to download a specific version of amrex run,

```bash
docker pull ghcr.io/autamus/amrex:21.06
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/amrex amrex --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/amrex bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the amrex container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/amrex amrex /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC amrex container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-amrex/).
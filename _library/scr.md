---
layout: container
name: scr
github: https://github.com/autamus/registry/blob/main/containers/s/scr/spack.yaml
versions:
- 3.0.rc.1
updated_at: 2021-10-22T14:47:48.620583603Z
size: 138MB
description: SCR caches checkpoint data in storage on the compute nodes of a Linux
  cluster to provide a fast, scalable checkpoint/restart capability for MPI codes
container_url: https://github.com/orgs/autamus/packages/container/package/scr

---
# scr
```bash 
Download        : docker pull ghcr.io/autamus/scr
Compressed Size : 138MB
```

## Description
SCR caches checkpoint data in storage on the compute nodes of a Linux cluster to provide a fast, scalable checkpoint/restart capability for MPI codes

## Usage
### Pull (Download)
To download the latest version of scr run,

```bash
docker pull ghcr.io/autamus/scr:latest
```

or to download a specific version of scr run,

```bash
docker pull ghcr.io/autamus/scr:3.0.rc.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/scr scr --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/scr bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the scr container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/scr scr /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC scr container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-scr/).
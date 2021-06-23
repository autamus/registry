---
layout: container
name: r
github: https://github.com/autamus/registry/blob/main/containers/r/r/spack.yaml
versions:
- 3.0.rc.1
- 4.0.4
updated_at: 2021-06-23T19:06:56.971142307Z
size: 273MB
description: SCR caches checkpoint data in storage on the compute nodes of a Linux
  cluster to provide a fast, scalable checkpoint/restart capability for MPI codes
container_url: https://github.com/orgs/autamus/packages/container/package/r

---
# r
```bash 
Download        : docker pull ghcr.io/autamus/r
Compressed Size : 273MB
```

## Description
SCR caches checkpoint data in storage on the compute nodes of a Linux cluster to provide a fast, scalable checkpoint/restart capability for MPI codes

## Usage
### Pull (Download)
To download the latest version of r run,

```bash
docker pull ghcr.io/autamus/r:latest
```

or to download a specific version of r run,

```bash
docker pull ghcr.io/autamus/r:3.0.rc.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/r r --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/r bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the r container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/r r /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC r container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-r/).
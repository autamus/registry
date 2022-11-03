---
layout: container
name: slepc
github: https://github.com/autamus/registry/blob/main/containers/s/slepc/spack.yaml
versions:
- 3.15.1
- 3.15.2
- 3.16.0
- 3.16.1
- 3.18.0
- 3.18.1
updated_at: 2022-11-03T21:42:58.159102505Z
size: 155MB
description: Scalable Library for Eigenvalue Problem Computations.
container_url: https://github.com/orgs/autamus/packages/container/package/slepc

---
# slepc
```bash 
Download        : docker pull ghcr.io/autamus/slepc
Compressed Size : 155MB
```

## Description
Scalable Library for Eigenvalue Problem Computations.

## Usage
### Pull (Download)
To download the latest version of slepc run,

```bash
docker pull ghcr.io/autamus/slepc:latest
```

or to download a specific version of slepc run,

```bash
docker pull ghcr.io/autamus/slepc:3.15.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/slepc slepc --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/slepc bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the slepc container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/slepc slepc /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC slepc container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-slepc/).
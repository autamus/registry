---
layout: container
name: ior
github: https://github.com/autamus/registry/blob/main/containers/i/ior/spack.yaml
versions:
- 3.3.0
updated_at: 2021-10-25T16:33:53.14325597Z
size: 52MB
description: The IOR software is used for benchmarking parallel file systems using
  POSIX, MPI-IO, or HDF5 interfaces.
container_url: https://github.com/orgs/autamus/packages/container/package/ior

---
# ior
```bash 
Download        : docker pull ghcr.io/autamus/ior
Compressed Size : 52MB
```

## Description
The IOR software is used for benchmarking parallel file systems using POSIX, MPI-IO, or HDF5 interfaces.

## Usage
### Pull (Download)
To download the latest version of ior run,

```bash
docker pull ghcr.io/autamus/ior:latest
```

or to download a specific version of ior run,

```bash
docker pull ghcr.io/autamus/ior:3.3.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/ior ior --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/ior bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the ior container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/ior ior /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC ior container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-ior/).
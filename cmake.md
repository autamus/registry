---
layout: container
name: cmake
github: https://github.com/autamus/registry/blob/main/containers/c/cmake/spack.yaml
versions:
- 3.21.0
updated_at: 2021-07-29T10:32:41.572766-07:00
size: 53MB
description: A cross-platform, open-source build system. CMake is a family of tools
  designed to build, test and package software.
container_url: https://github.com/orgs/autamus/packages/container/package/cmake

---
# cmake
```bash 
Download        : docker pull ghcr.io/autamus/cmake
Compressed Size : 54MB
```

## Description
A cross-platform, open-source build system. CMake is a family of tools designed to build, test and package software.

## Usage
### Pull (Download)
To download the latest version of cmake run,

```bash
docker pull ghcr.io/autamus/cmake:latest
```

or to download a specific version of cmake run,

```bash
docker pull ghcr.io/autamus/cmake:3.21.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/cmake cmake --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/cmake bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the cmake container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/cmake cmake /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC cmake container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-cmake/).

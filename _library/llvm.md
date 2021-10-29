---
layout: container
name: llvm
github: https://github.com/autamus/registry/blob/main/containers/l/llvm/spack.yaml
versions:
- 12.0.0
- 12.0.1
- 13.0.0
updated_at: 2021-10-29T15:38:59.158741632Z
size: 1961MB
description: ' homepage = "http://llvm.org/'
container_url: https://github.com/orgs/autamus/packages/container/package/llvm

---
# llvm
```bash 
Download        : docker pull ghcr.io/autamus/llvm
Compressed Size : 1961MB
```

## Description
 homepage = "http://llvm.org/

## Usage
### Pull (Download)
To download the latest version of llvm run,

```bash
docker pull ghcr.io/autamus/llvm:latest
```

or to download a specific version of llvm run,

```bash
docker pull ghcr.io/autamus/llvm:12.0.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/llvm llvm --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/llvm bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the llvm container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/llvm llvm /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC llvm container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-llvm/).
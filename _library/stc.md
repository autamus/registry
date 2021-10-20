---
layout: container
name: stc
github: https://github.com/autamus/registry/blob/main/containers/s/stc/spack.yaml
versions:
- 0.9.0
updated_at: 2021-10-20T03:36:09.719610848Z
size: 269MB
description: 'STC: The Swift-Turbine Compiler'
container_url: https://github.com/orgs/autamus/packages/container/package/stc

---
# stc
```bash 
Download        : docker pull ghcr.io/autamus/stc
Compressed Size : 269MB
```

## Description
STC: The Swift-Turbine Compiler

## Usage
### Pull (Download)
To download the latest version of stc run,

```bash
docker pull ghcr.io/autamus/stc:latest
```

or to download a specific version of stc run,

```bash
docker pull ghcr.io/autamus/stc:0.9.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/stc stc --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/stc bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the stc container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/stc stc /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC stc container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-stc/).
---
layout: container
name: binutils
github: https://github.com/autamus/registry/blob/main/containers/b/binutils/spack.yaml
versions:
- 2.36.1
- "2.37"
updated_at: 2021-09-15T23:33:46.090006424Z
size: 54MB
description: GNU binutils, which contain the linker, assembler, objdump and others
container_url: https://github.com/orgs/autamus/packages/container/package/binutils

---
# binutils
```bash 
Download        : docker pull ghcr.io/autamus/binutils
Compressed Size : 54MB
```

## Description
GNU binutils, which contain the linker, assembler, objdump and others

## Usage
### Pull (Download)
To download the latest version of binutils run,

```bash
docker pull ghcr.io/autamus/binutils:latest
```

or to download a specific version of binutils run,

```bash
docker pull ghcr.io/autamus/binutils:2.36.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/binutils binutils --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/binutils bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the binutils container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/binutils binutils /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC binutils container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-binutils/).
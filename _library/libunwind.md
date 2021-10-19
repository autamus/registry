---
layout: container
name: libunwind
github: https://github.com/autamus/registry/blob/main/containers/l/libunwind/spack.yaml
versions:
- "1.5"
updated_at: 2021-10-19T07:33:04.186167778Z
size: 27MB
description: A portable and efficient C programming interface (API) to determine the
  call-chain of a program.
container_url: https://github.com/orgs/autamus/packages/container/package/libunwind

---
# libunwind
```bash 
Download        : docker pull ghcr.io/autamus/libunwind
Compressed Size : 27MB
```

## Description
A portable and efficient C programming interface (API) to determine the call-chain of a program.

## Usage
### Pull (Download)
To download the latest version of libunwind run,

```bash
docker pull ghcr.io/autamus/libunwind:latest
```

or to download a specific version of libunwind run,

```bash
docker pull ghcr.io/autamus/libunwind:1.5
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/libunwind libunwind --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/libunwind bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the libunwind container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/libunwind libunwind /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC libunwind container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-libunwind/).
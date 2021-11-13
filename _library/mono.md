---
layout: container
name: mono
github: https://github.com/autamus/registry/blob/main/containers/m/mono/spack.yaml
versions:
- 6.12.0.122
- 6.8.0.123
updated_at: 2021-11-13T19:10:13.000059728Z
size: 146MB
description: 'Mono is a software platform designed to allow developers to easily create
  cross platform applications. It is an open source implementation of Microsoft''s
  .NET Framework based on the ECMA standards for C# and the Common Language Runtime. '
container_url: https://github.com/orgs/autamus/packages/container/package/mono

---
# mono
```bash 
Download        : docker pull ghcr.io/autamus/mono
Compressed Size : 146MB
```

## Description
Mono is a software platform designed to allow developers to easily create cross platform applications. It is an open source implementation of Microsoft's .NET Framework based on the ECMA standards for C# and the Common Language Runtime. 

## Usage
### Pull (Download)
To download the latest version of mono run,

```bash
docker pull ghcr.io/autamus/mono:latest
```

or to download a specific version of mono run,

```bash
docker pull ghcr.io/autamus/mono:6.12.0.122
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/mono mono --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/mono bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the mono container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/mono mono /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC mono container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-mono/).
---
layout: container
name: scons
github: https://github.com/autamus/registry/blob/main/containers/s/scons/spack.yaml
versions:
- 3.1.2
updated_at: 2021-10-19T07:54:02.022257844Z
size: 87MB
description: SCons is a software construction tool
container_url: https://github.com/orgs/autamus/packages/container/package/scons

---
# scons
```bash 
Download        : docker pull ghcr.io/autamus/scons
Compressed Size : 87MB
```

## Description
SCons is a software construction tool

## Usage
### Pull (Download)
To download the latest version of scons run,

```bash
docker pull ghcr.io/autamus/scons:latest
```

or to download a specific version of scons run,

```bash
docker pull ghcr.io/autamus/scons:3.1.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/scons scons --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/scons bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the scons container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/scons scons /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC scons container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-scons/).
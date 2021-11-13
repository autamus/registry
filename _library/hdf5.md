---
layout: container
name: hdf5
github: https://github.com/autamus/registry/blob/main/containers/h/hdf5/spack.yaml
versions:
- 1.12.0
- "1.13"
updated_at: 2021-11-13T18:52:05.964818188Z
size: 85MB
description: .format(version=str(spec.version.up_to(3))) with open("check.c", 'w
container_url: https://github.com/orgs/autamus/packages/container/package/hdf5

---
# hdf5
```bash 
Download        : docker pull ghcr.io/autamus/hdf5
Compressed Size : 85MB
```

## Description
.format(version=str(spec.version.up_to(3))) with open("check.c", 'w

## Usage
### Pull (Download)
To download the latest version of hdf5 run,

```bash
docker pull ghcr.io/autamus/hdf5:latest
```

or to download a specific version of hdf5 run,

```bash
docker pull ghcr.io/autamus/hdf5:1.12.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/hdf5 hdf5 --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/hdf5 bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the hdf5 container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/hdf5 hdf5 /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC hdf5 container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-hdf5/).
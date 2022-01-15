---
layout: container
name: openjdk
github: https://github.com/autamus/registry/blob/main/containers/o/openjdk/spack.yaml
versions:
- latest
updated_at: 2022-01-15T16:03:06.181547282Z
size: 218MB
description: The free and opensource java implementation
container_url: https://github.com/orgs/autamus/packages/container/package/openjdk

---
# openjdk
```bash 
Download        : docker pull ghcr.io/autamus/openjdk
Compressed Size : 218MB
```

## Description
The free and opensource java implementation

## Usage
### Pull (Download)
To download the latest version of openjdk run,

```bash
docker pull ghcr.io/autamus/openjdk:latest
```

or to download a specific version of openjdk run,

```bash
docker pull ghcr.io/autamus/openjdk:latest
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/openjdk openjdk --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/openjdk bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the openjdk container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/openjdk openjdk /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC openjdk container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-openjdk/).
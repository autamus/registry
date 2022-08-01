---
layout: container
name: alan
github: https://github.com/autamus/registry/blob/main/containers/a/alan/spack.yaml
versions:
- 2.1.1
updated_at: 2022-08-01T17:49:47.095719542Z
size: 26MB
description: Alignment viewer for linux terminal
container_url: https://github.com/orgs/autamus/packages/container/package/alan

---
# alan
```bash 
Download        : docker pull ghcr.io/autamus/alan
Compressed Size : 26MB
```

## Description
Alignment viewer for linux terminal

## Usage
### Pull (Download)
To download the latest version of alan run,

```bash
docker pull ghcr.io/autamus/alan:latest
```

or to download a specific version of alan run,

```bash
docker pull ghcr.io/autamus/alan:2.1.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/alan alan --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/alan bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the alan container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/alan alan /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC alan container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-alan/).
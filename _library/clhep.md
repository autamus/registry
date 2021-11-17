---
layout: container
name: clhep
github: https://github.com/autamus/registry/blob/main/containers/c/clhep/spack.yaml
versions:
- 2.4.4.0
updated_at: 2021-11-17T15:52:13.56426184Z
size: 29MB
description: 'CLHEP is a C++ Class Library for High Energy Physics. '
container_url: https://github.com/orgs/autamus/packages/container/package/clhep

---
# clhep
```bash 
Download        : docker pull ghcr.io/autamus/clhep
Compressed Size : 29MB
```

## Description
CLHEP is a C++ Class Library for High Energy Physics. 

## Usage
### Pull (Download)
To download the latest version of clhep run,

```bash
docker pull ghcr.io/autamus/clhep:latest
```

or to download a specific version of clhep run,

```bash
docker pull ghcr.io/autamus/clhep:2.4.4.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/clhep clhep --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/clhep bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the clhep container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/clhep clhep /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC clhep container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-clhep/).
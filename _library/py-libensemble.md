---
layout: container
name: py-libensemble
github: https://github.com/autamus/registry/blob/main/containers/p/py-libensemble/spack.yaml
versions:
- 0.7.2
- 0.8.0
updated_at: 2021-11-04T16:03:06.078991613Z
size: 118MB
description: Library for managing ensemble-like collections of computations.
container_url: https://github.com/orgs/autamus/packages/container/package/py-libensemble

---
# py-libensemble
```bash 
Download        : docker pull ghcr.io/autamus/py-libensemble
Compressed Size : 118MB
```

## Description
Library for managing ensemble-like collections of computations.

## Usage
### Pull (Download)
To download the latest version of py-libensemble run,

```bash
docker pull ghcr.io/autamus/py-libensemble:latest
```

or to download a specific version of py-libensemble run,

```bash
docker pull ghcr.io/autamus/py-libensemble:0.7.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/py-libensemble py-libensemble --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/py-libensemble bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the py-libensemble container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/py-libensemble py-libensemble /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC py-libensemble container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-py-libensemble/).
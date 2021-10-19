---
layout: container
name: siesta
github: https://github.com/autamus/registry/blob/main/containers/s/siesta/spack.yaml
versions:
- 4.0.2
updated_at: 2021-10-19T07:55:20.920243496Z
size: 119MB
description: SIESTA performs electronic structure calculations and ab initio molecular
  dynamics simulations of molecules and solids.
container_url: https://github.com/orgs/autamus/packages/container/package/siesta

---
# siesta
```bash 
Download        : docker pull ghcr.io/autamus/siesta
Compressed Size : 119MB
```

## Description
SIESTA performs electronic structure calculations and ab initio molecular dynamics simulations of molecules and solids.

## Usage
### Pull (Download)
To download the latest version of siesta run,

```bash
docker pull ghcr.io/autamus/siesta:latest
```

or to download a specific version of siesta run,

```bash
docker pull ghcr.io/autamus/siesta:4.0.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/siesta siesta --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/siesta bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the siesta container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/siesta siesta /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC siesta container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-siesta/).
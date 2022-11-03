---
layout: container
name: sundials
github: https://github.com/autamus/registry/blob/main/containers/s/sundials/spack.yaml
versions:
- 5.7.0
- latest
updated_at: 2022-11-03T00:34:40.113632969Z
size: 68MB
description: SUNDIALS (SUite of Nonlinear and DIfferential/ALgebraic equation Solvers
container_url: https://github.com/orgs/autamus/packages/container/package/sundials

---
# sundials
```bash 
Download        : docker pull ghcr.io/autamus/sundials
Compressed Size : 68MB
```

## Description
SUNDIALS (SUite of Nonlinear and DIfferential/ALgebraic equation Solvers

## Usage
### Pull (Download)
To download the latest version of sundials run,

```bash
docker pull ghcr.io/autamus/sundials:latest
```

or to download a specific version of sundials run,

```bash
docker pull ghcr.io/autamus/sundials:5.7.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/sundials sundials --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/sundials bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the sundials container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/sundials sundials /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC sundials container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-sundials/).
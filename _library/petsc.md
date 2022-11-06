---
layout: container
name: petsc
github: https://github.com/autamus/registry/blob/main/containers/p/petsc/spack.yaml
versions:
- 3.15.1
- 3.15.2
- 3.15.3
- 3.15.4
- 3.16.0
- 3.16.1
- 3.16.2
- 3.16.3
- 3.18.1
updated_at: 2022-11-06T21:27:36.284272168Z
size: 148MB
description: 'PETSc is a suite of data structures and routines for the scalable (parallel)
  solution of scientific applications modeled by partial differential equations. '
container_url: https://github.com/orgs/autamus/packages/container/package/petsc

---
# petsc
```bash 
Download        : docker pull ghcr.io/autamus/petsc
Compressed Size : 148MB
```

## Description
PETSc is a suite of data structures and routines for the scalable (parallel) solution of scientific applications modeled by partial differential equations. 

## Usage
### Pull (Download)
To download the latest version of petsc run,

```bash
docker pull ghcr.io/autamus/petsc:latest
```

or to download a specific version of petsc run,

```bash
docker pull ghcr.io/autamus/petsc:3.15.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/petsc petsc --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/petsc bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the petsc container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/petsc petsc /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC petsc container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-petsc/).
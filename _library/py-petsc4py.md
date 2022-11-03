---
layout: container
name: py-petsc4py
github: https://github.com/autamus/registry/blob/main/containers/p/py-petsc4py/spack.yaml
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
updated_at: 2022-11-03T00:28:09.146262051Z
size: 204MB
description: 'This package provides Python bindings for the PETSc package. '
container_url: https://github.com/orgs/autamus/packages/container/package/py-petsc4py

---
# py-petsc4py
```bash 
Download        : docker pull ghcr.io/autamus/py-petsc4py
Compressed Size : 204MB
```

## Description
This package provides Python bindings for the PETSc package. 

## Usage
### Pull (Download)
To download the latest version of py-petsc4py run,

```bash
docker pull ghcr.io/autamus/py-petsc4py:latest
```

or to download a specific version of py-petsc4py run,

```bash
docker pull ghcr.io/autamus/py-petsc4py:3.15.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/py-petsc4py py-petsc4py --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/py-petsc4py bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the py-petsc4py container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/py-petsc4py py-petsc4py /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC py-petsc4py container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-py-petsc4py/).
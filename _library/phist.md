---
layout: container
name: phist
github: https://github.com/autamus/registry/blob/main/containers/p/phist/spack.yaml
versions:
- 1.9.4
- 1.9.5
- 1.9.6
updated_at: 2021-10-19T07:46:53.700290861Z
size: 77MB
description: 'The Pipelined, Hybrid-parallel Iterative Solver Toolkit provides implementations
  of and interfaces to block iterative solvers for sparse linear and eigenvalue problems.
  In contrast to other libraries we support multiple backends (e.g. Trilinos, PETSc
  and our own optimized kernels), and interfaces in multiple languages such as C,
  C++, Fortran 2003 and Python. PHIST has a clear focus on portability and hardware
  performance: in particular support row-major storage of block vectors and using
  GPUs (via the ghost library or Trilinos/Tpetra). '
container_url: https://github.com/orgs/autamus/packages/container/package/phist

---
# phist
```bash 
Download        : docker pull ghcr.io/autamus/phist
Compressed Size : 77MB
```

## Description
The Pipelined, Hybrid-parallel Iterative Solver Toolkit provides implementations of and interfaces to block iterative solvers for sparse linear and eigenvalue problems. In contrast to other libraries we support multiple backends (e.g. Trilinos, PETSc and our own optimized kernels), and interfaces in multiple languages such as C, C++, Fortran 2003 and Python. PHIST has a clear focus on portability and hardware performance: in particular support row-major storage of block vectors and using GPUs (via the ghost library or Trilinos/Tpetra). 

## Usage
### Pull (Download)
To download the latest version of phist run,

```bash
docker pull ghcr.io/autamus/phist:latest
```

or to download a specific version of phist run,

```bash
docker pull ghcr.io/autamus/phist:1.9.4
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/phist phist --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/phist bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the phist container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/phist phist /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC phist container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-phist/).
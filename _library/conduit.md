---
layout: container
name: conduit
github: https://github.com/autamus/registry/blob/main/containers/c/conduit/spack.yaml
versions:
- 0.7.2
updated_at: 2021-10-19T07:22:45.918449346Z
size: 71MB
description: Conduit is an open source project from Lawrence Livermore National Laboratory
  that provides an intuitive model for describing hierarchical scientific data in
  C++, C, Fortran, and Python. It is used for data coupling between packages in-core,
  serialization, and I/O tasks.
container_url: https://github.com/orgs/autamus/packages/container/package/conduit

---
# conduit
```bash 
Download        : docker pull ghcr.io/autamus/conduit
Compressed Size : 71MB
```

## Description
Conduit is an open source project from Lawrence Livermore National Laboratory that provides an intuitive model for describing hierarchical scientific data in C++, C, Fortran, and Python. It is used for data coupling between packages in-core, serialization, and I/O tasks.

## Usage
### Pull (Download)
To download the latest version of conduit run,

```bash
docker pull ghcr.io/autamus/conduit:latest
```

or to download a specific version of conduit run,

```bash
docker pull ghcr.io/autamus/conduit:0.7.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/conduit conduit --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/conduit bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the conduit container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/conduit conduit /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC conduit container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-conduit/).
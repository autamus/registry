---
layout: container
name: cfitsio
github: https://github.com/autamus/registry/blob/main/containers/c/cfitsio/spack.yaml
versions:
- "3.49"
- 4.0.0
updated_at: 2021-10-19T07:18:55.783706563Z
size: 33MB
description: 'CFITSIO is a library of C and Fortran subroutines for reading and writing
  data files in FITS (Flexible Image Transport System) data format. '
container_url: https://github.com/orgs/autamus/packages/container/package/cfitsio

---
# cfitsio
```bash 
Download        : docker pull ghcr.io/autamus/cfitsio
Compressed Size : 33MB
```

## Description
CFITSIO is a library of C and Fortran subroutines for reading and writing data files in FITS (Flexible Image Transport System) data format. 

## Usage
### Pull (Download)
To download the latest version of cfitsio run,

```bash
docker pull ghcr.io/autamus/cfitsio:latest
```

or to download a specific version of cfitsio run,

```bash
docker pull ghcr.io/autamus/cfitsio:3.49
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/cfitsio cfitsio --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/cfitsio bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the cfitsio container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/cfitsio cfitsio /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC cfitsio container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-cfitsio/).
---
layout: container
name: pdt
github: https://github.com/autamus/registry/blob/main/containers/p/pdt/spack.yaml
versions:
- 3.25.1
updated_at: 2021-10-19T07:43:10.75421173Z
size: 81MB
description: 'Program Database Toolkit (PDT) is a framework for analyzing source code
  written in several programming languages and for making rich program knowledge accessible
  to developers of static and dynamic analysis tools. PDT implements a standard program
  representation, the program database (PDB), that can be accessed in a uniform way
  through a class library supporting common PDB operations. '
container_url: https://github.com/orgs/autamus/packages/container/package/pdt

---
# pdt
```bash 
Download        : docker pull ghcr.io/autamus/pdt
Compressed Size : 81MB
```

## Description
Program Database Toolkit (PDT) is a framework for analyzing source code written in several programming languages and for making rich program knowledge accessible to developers of static and dynamic analysis tools. PDT implements a standard program representation, the program database (PDB), that can be accessed in a uniform way through a class library supporting common PDB operations. 

## Usage
### Pull (Download)
To download the latest version of pdt run,

```bash
docker pull ghcr.io/autamus/pdt:latest
```

or to download a specific version of pdt run,

```bash
docker pull ghcr.io/autamus/pdt:3.25.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/pdt pdt --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/pdt bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the pdt container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/pdt pdt /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC pdt container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-pdt/).
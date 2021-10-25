---
layout: container
name: python
github: https://github.com/autamus/registry/blob/main/containers/p/python/spack.yaml
versions:
- 3.9.5
- 3.9.6
- 3.9.7
updated_at: 2021-10-25T16:43:56.484386994Z
size: 84MB
description: The Python programming language.
container_url: https://github.com/orgs/autamus/packages/container/package/python

---
# python
```bash 
Download        : docker pull ghcr.io/autamus/python
Compressed Size : 84MB
```

## Description
The Python programming language.

## Usage
### Pull (Download)
To download the latest version of python run,

```bash
docker pull ghcr.io/autamus/python:latest
```

or to download a specific version of python run,

```bash
docker pull ghcr.io/autamus/python:3.9.5
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/python python --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/python bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the python container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/python python /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC python container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-python/).
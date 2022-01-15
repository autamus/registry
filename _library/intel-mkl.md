---
layout: container
name: intel-mkl
github: https://github.com/autamus/registry/blob/main/containers/i/intel-mkl/spack.yaml
versions:
- 2020.4.304
updated_at: 2022-01-15T16:04:39.438098809Z
size: 1091MB
description: Intel Math Kernel Library.
container_url: https://github.com/orgs/autamus/packages/container/package/intel-mkl

---
# intel-mkl
```bash 
Download        : docker pull ghcr.io/autamus/intel-mkl
Compressed Size : 1091MB
```

## Description
Intel Math Kernel Library.

## Usage
### Pull (Download)
To download the latest version of intel-mkl run,

```bash
docker pull ghcr.io/autamus/intel-mkl:latest
```

or to download a specific version of intel-mkl run,

```bash
docker pull ghcr.io/autamus/intel-mkl:2020.4.304
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/intel-mkl intel-mkl --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/intel-mkl bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the intel-mkl container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/intel-mkl intel-mkl /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC intel-mkl container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-intel-mkl/).
---
layout: container
name: mfem
github: https://github.com/autamus/registry/blob/main/containers/m/mfem/spack.yaml
versions:
- 4.2.0
- 4.3.0
updated_at: 2021-10-19T07:38:49.975801653Z
size: 87MB
description: Free, lightweight, scalable C++ library for finite element methods.
container_url: https://github.com/orgs/autamus/packages/container/package/mfem

---
# mfem
```bash 
Download        : docker pull ghcr.io/autamus/mfem
Compressed Size : 87MB
```

## Description
Free, lightweight, scalable C++ library for finite element methods.

## Usage
### Pull (Download)
To download the latest version of mfem run,

```bash
docker pull ghcr.io/autamus/mfem:latest
```

or to download a specific version of mfem run,

```bash
docker pull ghcr.io/autamus/mfem:4.2.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/mfem mfem --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/mfem bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the mfem container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/mfem mfem /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC mfem container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-mfem/).
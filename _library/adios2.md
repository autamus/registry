---
layout: container
name: adios2
github: https://github.com/autamus/registry/blob/main/containers/a/adios2/spack.yaml
versions:
- 2.7.1
updated_at: 2021-10-25T16:24:39.280215214Z
size: 61MB
description: The Adaptable Input Output System version 2, developed in the Exascale
  Computing Program
container_url: https://github.com/orgs/autamus/packages/container/package/adios2

---
# adios2
```bash 
Download        : docker pull ghcr.io/autamus/adios2
Compressed Size : 61MB
```

## Description
The Adaptable Input Output System version 2, developed in the Exascale Computing Program

## Usage
### Pull (Download)
To download the latest version of adios2 run,

```bash
docker pull ghcr.io/autamus/adios2:latest
```

or to download a specific version of adios2 run,

```bash
docker pull ghcr.io/autamus/adios2:2.7.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/adios2 adios2 --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/adios2 bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the adios2 container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/adios2 adios2 /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC adios2 container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-adios2/).
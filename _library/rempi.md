---
layout: container
name: rempi
github: https://github.com/autamus/registry/blob/main/containers/r/rempi/spack.yaml
versions:
- 1.1.0
updated_at: 2021-10-19T07:51:40.632982688Z
size: 52MB
description: ReMPI is a record-and-replay tool for MPI applications.
container_url: https://github.com/orgs/autamus/packages/container/package/rempi

---
# rempi
```bash 
Download        : docker pull ghcr.io/autamus/rempi
Compressed Size : 52MB
```

## Description
ReMPI is a record-and-replay tool for MPI applications.

## Usage
### Pull (Download)
To download the latest version of rempi run,

```bash
docker pull ghcr.io/autamus/rempi:latest
```

or to download a specific version of rempi run,

```bash
docker pull ghcr.io/autamus/rempi:1.1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/rempi rempi --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/rempi bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the rempi container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/rempi rempi /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC rempi container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-rempi/).
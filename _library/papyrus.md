---
layout: container
name: papyrus
github: https://github.com/autamus/registry/blob/main/containers/p/papyrus/spack.yaml
versions:
- 1.0.2
updated_at: 2021-09-01T18:51:45.712822844Z
size: 52MB
description: Parallel Aggregate Persistent Storage
container_url: https://github.com/orgs/autamus/packages/container/package/papyrus

---
# papyrus
```bash 
Download        : docker pull ghcr.io/autamus/papyrus
Compressed Size : 52MB
```

## Description
Parallel Aggregate Persistent Storage

## Usage
### Pull (Download)
To download the latest version of papyrus run,

```bash
docker pull ghcr.io/autamus/papyrus:latest
```

or to download a specific version of papyrus run,

```bash
docker pull ghcr.io/autamus/papyrus:1.0.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/papyrus papyrus --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/papyrus bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the papyrus container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/papyrus papyrus /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC papyrus container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-papyrus/).
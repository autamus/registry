---
layout: container
name: sparse
github: https://github.com/autamus/registry/blob/main/containers/s/sparse/spack.yaml
versions:
- "1.4"
updated_at: 2022-01-15T16:09:57.994066343Z
size: 26MB
description: An open source sparse linear equation solver.
container_url: https://github.com/orgs/autamus/packages/container/package/sparse

---
# sparse
```bash 
Download        : docker pull ghcr.io/autamus/sparse
Compressed Size : 26MB
```

## Description
An open source sparse linear equation solver.

## Usage
### Pull (Download)
To download the latest version of sparse run,

```bash
docker pull ghcr.io/autamus/sparse:latest
```

or to download a specific version of sparse run,

```bash
docker pull ghcr.io/autamus/sparse:1.4
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/sparse sparse --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/sparse bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the sparse container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/sparse sparse /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC sparse container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-sparse/).
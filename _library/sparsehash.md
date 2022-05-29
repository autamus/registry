---
layout: container
name: sparsehash
github: https://github.com/autamus/registry/blob/main/containers/s/sparsehash/spack.yaml
versions:
- 2.0.3
- 2.0.4
updated_at: 2022-05-29T19:33:10.700754861Z
size: 27MB
description: Sparse and dense hash-tables for C++ by Google
container_url: https://github.com/orgs/autamus/packages/container/package/sparsehash

---
# sparsehash
```bash 
Download        : docker pull ghcr.io/autamus/sparsehash
Compressed Size : 27MB
```

## Description
Sparse and dense hash-tables for C++ by Google

## Usage
### Pull (Download)
To download the latest version of sparsehash run,

```bash
docker pull ghcr.io/autamus/sparsehash:latest
```

or to download a specific version of sparsehash run,

```bash
docker pull ghcr.io/autamus/sparsehash:2.0.3
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/sparsehash sparsehash --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/sparsehash bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the sparsehash container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/sparsehash sparsehash /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC sparsehash container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-sparsehash/).
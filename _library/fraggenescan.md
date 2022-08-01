---
layout: container
name: fraggenescan
github: https://github.com/autamus/registry/blob/main/containers/f/fraggenescan/spack.yaml
versions:
- "1.31"
updated_at: 2022-08-01T18:28:13.182056818Z
size: 66MB
description: FragGeneScan is an application for finding (fragmented) genes in short
  reads. It can also be applied to predict prokaryotic genes in incomplete assemblies
  or complete genomes.
container_url: https://github.com/orgs/autamus/packages/container/package/fraggenescan

---
# fraggenescan
```bash 
Download        : docker pull ghcr.io/autamus/fraggenescan
Compressed Size : 66MB
```

## Description
FragGeneScan is an application for finding (fragmented) genes in short reads. It can also be applied to predict prokaryotic genes in incomplete assemblies or complete genomes.

## Usage
### Pull (Download)
To download the latest version of fraggenescan run,

```bash
docker pull ghcr.io/autamus/fraggenescan:latest
```

or to download a specific version of fraggenescan run,

```bash
docker pull ghcr.io/autamus/fraggenescan:1.31
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/fraggenescan fraggenescan --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/fraggenescan bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the fraggenescan container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/fraggenescan fraggenescan /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC fraggenescan container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-fraggenescan/).
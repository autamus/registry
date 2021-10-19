---
layout: container
name: cdo
github: https://github.com/autamus/registry/blob/main/containers/c/cdo/spack.yaml
versions:
- 1.9.10
updated_at: 2021-10-19T07:22:38.320825769Z
size: 118MB
description: 'CDO is a collection of command line Operators to manipulate and analyse
  Climate and NWP model Data. '
container_url: https://github.com/orgs/autamus/packages/container/package/cdo

---
# cdo
```bash 
Download        : docker pull ghcr.io/autamus/cdo
Compressed Size : 118MB
```

## Description
CDO is a collection of command line Operators to manipulate and analyse Climate and NWP model Data. 

## Usage
### Pull (Download)
To download the latest version of cdo run,

```bash
docker pull ghcr.io/autamus/cdo:latest
```

or to download a specific version of cdo run,

```bash
docker pull ghcr.io/autamus/cdo:1.9.10
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/cdo cdo --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/cdo bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the cdo container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/cdo cdo /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC cdo container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-cdo/).
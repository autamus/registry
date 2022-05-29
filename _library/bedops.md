---
layout: container
name: bedops
github: https://github.com/autamus/registry/blob/main/containers/b/bedops/spack.yaml
versions:
- 2.4.35
- 2.4.39
- 2.4.40
updated_at: 2022-05-29T17:40:00.84749093Z
size: 30MB
description: BEDOPS is an open-source command-line toolkit that performs highly efficient
  and scalable Boolean and other set operations, statistical calculations, archiving,
  conversion and other management of genomic data of arbitrary scale.
container_url: https://github.com/orgs/autamus/packages/container/package/bedops

---
# bedops
```bash 
Download        : docker pull ghcr.io/autamus/bedops
Compressed Size : 30MB
```

## Description
BEDOPS is an open-source command-line toolkit that performs highly efficient and scalable Boolean and other set operations, statistical calculations, archiving, conversion and other management of genomic data of arbitrary scale.

## Usage
### Pull (Download)
To download the latest version of bedops run,

```bash
docker pull ghcr.io/autamus/bedops:latest
```

or to download a specific version of bedops run,

```bash
docker pull ghcr.io/autamus/bedops:2.4.35
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/bedops bedops --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/bedops bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the bedops container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/bedops bedops /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC bedops container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-bedops/).
---
layout: container
name: mummer
github: https://github.com/autamus/registry/blob/main/containers/m/mummer/spack.yaml
versions:
- "3.23"
updated_at: 2021-10-19T07:46:32.649119566Z
size: 177MB
description: MUMmer is a system for rapidly aligning entire genomes.
container_url: https://github.com/orgs/autamus/packages/container/package/mummer

---
# mummer
```bash 
Download        : docker pull ghcr.io/autamus/mummer
Compressed Size : 177MB
```

## Description
MUMmer is a system for rapidly aligning entire genomes.

## Usage
### Pull (Download)
To download the latest version of mummer run,

```bash
docker pull ghcr.io/autamus/mummer:latest
```

or to download a specific version of mummer run,

```bash
docker pull ghcr.io/autamus/mummer:3.23
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/mummer mummer --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/mummer bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the mummer container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/mummer mummer /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC mummer container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-mummer/).
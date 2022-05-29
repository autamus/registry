---
layout: container
name: prodigal
github: https://github.com/autamus/registry/blob/main/containers/p/prodigal/spack.yaml
versions:
- 2.6.3
updated_at: 2022-05-29T19:06:29.257325901Z
size: 27MB
description: Fast, reliable protein-coding gene prediction for prokaryotic genomes.
container_url: https://github.com/orgs/autamus/packages/container/package/prodigal

---
# prodigal
```bash 
Download        : docker pull ghcr.io/autamus/prodigal
Compressed Size : 27MB
```

## Description
Fast, reliable protein-coding gene prediction for prokaryotic genomes.

## Usage
### Pull (Download)
To download the latest version of prodigal run,

```bash
docker pull ghcr.io/autamus/prodigal:latest
```

or to download a specific version of prodigal run,

```bash
docker pull ghcr.io/autamus/prodigal:2.6.3
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/prodigal prodigal --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/prodigal bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the prodigal container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/prodigal prodigal /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC prodigal container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-prodigal/).
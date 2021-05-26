---
layout: container
name: hisat2
github: https://github.com/autamus/registry/blob/main/containers/h/hisat2/spack.yaml
versions:
- 2.2.0
updated_at: 2021-05-26T06:18:27.848994107Z
size: 32MB
description: HISAT2 is a fast and sensitive alignment program for mapping next-generation
  sequencing reads (whole-genome, transcriptome, and exome sequencing data) against
  the general human population (as well as against a single reference genome).
container_url: https://github.com/orgs/autamus/packages/container/package/hisat2

---
# hisat2
```bash 
Download        : docker pull ghcr.io/autamus/hisat2
Compressed Size : 32MB
```

## Description
HISAT2 is a fast and sensitive alignment program for mapping next-generation sequencing reads (whole-genome, transcriptome, and exome sequencing data) against the general human population (as well as against a single reference genome).

## Usage
### Pull (Download)
To download the latest version of hisat2 run,

```bash
docker pull ghcr.io/autamus/hisat2:latest
```

or to download a specific version of hisat2 run,

```bash
docker pull ghcr.io/autamus/hisat2:2.2.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/hisat2 hisat2 --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/hisat2 bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the hisat2 container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/hisat2 hisat2 /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC hisat2 container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-hisat2/).
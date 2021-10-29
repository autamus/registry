---
layout: container
name: hmmer
github: https://github.com/autamus/registry/blob/main/containers/h/hmmer/spack.yaml
versions:
- 3.3.2
updated_at: 2021-10-29T15:02:04.12188403Z
size: 59MB
description: 'HMMER is used for searching sequence databases for sequence homologs,
  and for making sequence alignments. It implements methods using probabilistic models
  called profile hidden Markov models (profile HMMs). '
container_url: https://github.com/orgs/autamus/packages/container/package/hmmer

---
# hmmer
```bash 
Download        : docker pull ghcr.io/autamus/hmmer
Compressed Size : 59MB
```

## Description
HMMER is used for searching sequence databases for sequence homologs, and for making sequence alignments. It implements methods using probabilistic models called profile hidden Markov models (profile HMMs). 

## Usage
### Pull (Download)
To download the latest version of hmmer run,

```bash
docker pull ghcr.io/autamus/hmmer:latest
```

or to download a specific version of hmmer run,

```bash
docker pull ghcr.io/autamus/hmmer:3.3.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/hmmer hmmer --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/hmmer bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the hmmer container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/hmmer hmmer /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC hmmer container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-hmmer/).
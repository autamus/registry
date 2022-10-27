---
layout: container
name: bwa
github: https://github.com/autamus/registry/blob/main/containers/b/bwa/spack.yaml
versions:
- 0.7.17
updated_at: 2022-10-27T17:03:15.872782618Z
size: 27MB
description: Burrow-Wheeler Aligner for pairwise alignment between DNA sequences.
container_url: https://github.com/orgs/autamus/packages/container/package/bwa

---
# bwa
```bash 
Download        : docker pull ghcr.io/autamus/bwa
Compressed Size : 27MB
```

## Description
Burrow-Wheeler Aligner for pairwise alignment between DNA sequences.

## Usage
### Pull (Download)
To download the latest version of bwa run,

```bash
docker pull ghcr.io/autamus/bwa:latest
```

or to download a specific version of bwa run,

```bash
docker pull ghcr.io/autamus/bwa:0.7.17
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/bwa bwa --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/bwa bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the bwa container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/bwa bwa /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC bwa container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-bwa/).
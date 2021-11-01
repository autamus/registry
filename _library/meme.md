---
layout: container
name: meme
github: https://github.com/autamus/registry/blob/main/containers/m/meme/spack.yaml
versions:
- 5.3.0
updated_at: 2021-11-01T16:09:11.74920041Z
size: 138MB
description: The MEME Suite allows the biologist to discover novel motifs in collections
  of unaligned nucleotide or protein sequences, and to perform a wide variety of other
  motif-based analyses.
container_url: https://github.com/orgs/autamus/packages/container/package/meme

---
# meme
```bash 
Download        : docker pull ghcr.io/autamus/meme
Compressed Size : 138MB
```

## Description
The MEME Suite allows the biologist to discover novel motifs in collections of unaligned nucleotide or protein sequences, and to perform a wide variety of other motif-based analyses.

## Usage
### Pull (Download)
To download the latest version of meme run,

```bash
docker pull ghcr.io/autamus/meme:latest
```

or to download a specific version of meme run,

```bash
docker pull ghcr.io/autamus/meme:5.3.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/meme meme --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/meme bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the meme container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/meme meme /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC meme container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-meme/).
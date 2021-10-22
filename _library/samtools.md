---
layout: container
name: samtools
github: https://github.com/autamus/registry/blob/main/containers/s/samtools/spack.yaml
versions:
- "1.12"
- "1.13"
- "1.14"
updated_at: 2021-10-22T19:34:36.142571763Z
size: 106MB
description: SAM Tools provide various utilities for manipulating alignments in the
  SAM format, including sorting, merging, indexing and generating alignments in a
  per-position format
container_url: https://github.com/orgs/autamus/packages/container/package/samtools

---
# samtools
```bash 
Download        : docker pull ghcr.io/autamus/samtools
Compressed Size : 106MB
```

## Description
SAM Tools provide various utilities for manipulating alignments in the SAM format, including sorting, merging, indexing and generating alignments in a per-position format

## Usage
### Pull (Download)
To download the latest version of samtools run,

```bash
docker pull ghcr.io/autamus/samtools:latest
```

or to download a specific version of samtools run,

```bash
docker pull ghcr.io/autamus/samtools:1.12
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/samtools samtools --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/samtools bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the samtools container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/samtools samtools /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC samtools container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-samtools/).
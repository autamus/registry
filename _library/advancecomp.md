---
layout: container
name: advancecomp
github: https://github.com/autamus/registry/blob/main/containers/a/advancecomp/spack.yaml
versions:
- "2.1"
updated_at: 2021-10-29T14:57:11.671853136Z
size: 27MB
description: AdvanceCOMP contains recompression utilities for your .zip archives,
  .png images, .mng video clips and .gz files.
container_url: https://github.com/orgs/autamus/packages/container/package/advancecomp

---
# advancecomp
```bash 
Download        : docker pull ghcr.io/autamus/advancecomp
Compressed Size : 27MB
```

## Description
AdvanceCOMP contains recompression utilities for your .zip archives, .png images, .mng video clips and .gz files.

## Usage
### Pull (Download)
To download the latest version of advancecomp run,

```bash
docker pull ghcr.io/autamus/advancecomp:latest
```

or to download a specific version of advancecomp run,

```bash
docker pull ghcr.io/autamus/advancecomp:2.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/advancecomp advancecomp --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/advancecomp bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the advancecomp container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/advancecomp advancecomp /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC advancecomp container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-advancecomp/).
---
layout: container
name: salmon
github: https://github.com/autamus/registry/blob/main/containers/s/salmon/spack.yaml
versions:
- 1.4.0
- 1.5.2
updated_at: 2021-10-25T16:45:35.795777212Z
size: 60MB
description: Salmon is a tool for quantifying the expression of transcripts using
  RNA-seq data.
container_url: https://github.com/orgs/autamus/packages/container/package/salmon

---
# salmon
```bash 
Download        : docker pull ghcr.io/autamus/salmon
Compressed Size : 60MB
```

## Description
Salmon is a tool for quantifying the expression of transcripts using RNA-seq data.

## Usage
### Pull (Download)
To download the latest version of salmon run,

```bash
docker pull ghcr.io/autamus/salmon:latest
```

or to download a specific version of salmon run,

```bash
docker pull ghcr.io/autamus/salmon:1.4.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/salmon salmon --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/salmon bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the salmon container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/salmon salmon /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC salmon container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-salmon/).
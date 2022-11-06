---
layout: container
name: r-seqlogo
github: https://github.com/autamus/registry/blob/main/containers/r/r-seqlogo/spack.yaml
versions:
- 1.56.0
- 1.62.0
updated_at: 2022-11-06T20:50:09.362250453Z
size: 277MB
description: Sequence logos for DNA sequence alignments seqLogo takes the position
  weight matrix of a DNA sequence motif and plots the corresponding sequence logo
  as introduced by Schneider and Stephens (1990).
container_url: https://github.com/orgs/autamus/packages/container/package/r-seqlogo

---
# r-seqlogo
```bash 
Download        : docker pull ghcr.io/autamus/r-seqlogo
Compressed Size : 277MB
```

## Description
Sequence logos for DNA sequence alignments seqLogo takes the position weight matrix of a DNA sequence motif and plots the corresponding sequence logo as introduced by Schneider and Stephens (1990).

## Usage
### Pull (Download)
To download the latest version of r-seqlogo run,

```bash
docker pull ghcr.io/autamus/r-seqlogo:latest
```

or to download a specific version of r-seqlogo run,

```bash
docker pull ghcr.io/autamus/r-seqlogo:1.56.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/r-seqlogo r-seqlogo --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/r-seqlogo bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the r-seqlogo container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/r-seqlogo r-seqlogo /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC r-seqlogo container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-r-seqlogo/).
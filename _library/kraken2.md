---
layout: container
name: kraken2
github: https://github.com/autamus/registry/blob/main/containers/k/kraken2/spack.yaml
versions:
- 2.1.1
- 2.1.2
updated_at: 2021-11-01T16:04:28.201321147Z
size: 56MB
description: Kraken2 is a system for assigning taxonomic labels to short DNA sequences,
  usually obtained through metagenomic studies.
container_url: https://github.com/orgs/autamus/packages/container/package/kraken2

---
# kraken2
```bash 
Download        : docker pull ghcr.io/autamus/kraken2
Compressed Size : 56MB
```

## Description
Kraken2 is a system for assigning taxonomic labels to short DNA sequences, usually obtained through metagenomic studies.

## Usage
### Pull (Download)
To download the latest version of kraken2 run,

```bash
docker pull ghcr.io/autamus/kraken2:latest
```

or to download a specific version of kraken2 run,

```bash
docker pull ghcr.io/autamus/kraken2:2.1.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/kraken2 kraken2 --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/kraken2 bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the kraken2 container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/kraken2 kraken2 /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC kraken2 container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-kraken2/).
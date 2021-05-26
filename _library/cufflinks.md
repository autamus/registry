---
layout: container
name: cufflinks
github: https://github.com/autamus/registry/blob/main/containers/c/cufflinks/spack.yaml
versions:
- 2.2.1
updated_at: 2021-05-26T04:30:43.261624996Z
size: 32MB
description: Cufflinks assembles transcripts, estimates their abundances, and tests
  for differential expression and regulation in RNA-Seq samples.
container_url: https://github.com/orgs/autamus/packages/container/package/cufflinks

---
# cufflinks
```bash 
Download        : docker pull ghcr.io/autamus/cufflinks
Compressed Size : 32MB
```

## Description
Cufflinks assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples.

## Usage
### Pull (Download)
To download the latest version of cufflinks run,

```bash
docker pull ghcr.io/autamus/cufflinks:latest
```

or to download a specific version of cufflinks run,

```bash
docker pull ghcr.io/autamus/cufflinks:2.2.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/cufflinks cufflinks --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/cufflinks bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the cufflinks container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/cufflinks cufflinks /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC cufflinks container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-cufflinks/).
---
layout: container
name: bowtie2
github: https://github.com/autamus/registry/blob/main/containers/b/bowtie2/spack.yaml
versions:
- 2.4.2
updated_at: 2022-01-09T16:15:11.748774Z
size: 107MB
description: Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing
  reads to long reference sequences
container_url: https://github.com/orgs/autamus/packages/container/package/bowtie2

---
# bowtie2
```bash 
Download        : docker pull ghcr.io/autamus/bowtie2
Compressed Size : 107MB
```

## Description
Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences

## Usage
### Pull (Download)
To download the latest version of bowtie2 run,

```bash
docker pull ghcr.io/autamus/bowtie2:latest
```

or to download a specific version of bowtie2 run,

```bash
docker pull ghcr.io/autamus/bowtie2:2.4.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/bowtie2 bowtie2 --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/bowtie2 bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the bowtie2 container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/bowtie2 bowtie2 /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC bowtie2 container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-bowtie2/).
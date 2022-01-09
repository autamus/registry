---
layout: container
name: bedtools2
github: https://github.com/autamus/registry/blob/main/containers/b/bedtools2/spack.yaml
versions:
- 2.30.0
updated_at: 2022-01-09T16:13:25.440169907Z
size: 28MB
description: 'Collectively, the bedtools utilities are a swiss-army knife of tools
  for a wide-range of genomics analysis tasks. The most widely-used tools enable genome
  arithmetic: that is, set theory on the genome.'
container_url: https://github.com/orgs/autamus/packages/container/package/bedtools2

---
# bedtools2
```bash 
Download        : docker pull ghcr.io/autamus/bedtools2
Compressed Size : 28MB
```

## Description
Collectively, the bedtools utilities are a swiss-army knife of tools for a wide-range of genomics analysis tasks. The most widely-used tools enable genome arithmetic: that is, set theory on the genome.

## Usage
### Pull (Download)
To download the latest version of bedtools2 run,

```bash
docker pull ghcr.io/autamus/bedtools2:latest
```

or to download a specific version of bedtools2 run,

```bash
docker pull ghcr.io/autamus/bedtools2:2.30.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/bedtools2 bedtools2 --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/bedtools2 bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the bedtools2 container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/bedtools2 bedtools2 /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC bedtools2 container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-bedtools2/).
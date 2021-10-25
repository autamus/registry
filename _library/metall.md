---
layout: container
name: metall
github: https://github.com/autamus/registry/blob/main/containers/m/metall/spack.yaml
versions:
- "0.13"
- "0.15"
- "0.16"
- "0.17"
updated_at: 2021-10-25T16:36:19.310713461Z
size: 48MB
description: A Persistent Memory Allocator For Data-Centric Analytics
container_url: https://github.com/orgs/autamus/packages/container/package/metall

---
# metall
```bash 
Download        : docker pull ghcr.io/autamus/metall
Compressed Size : 48MB
```

## Description
A Persistent Memory Allocator For Data-Centric Analytics

## Usage
### Pull (Download)
To download the latest version of metall run,

```bash
docker pull ghcr.io/autamus/metall:latest
```

or to download a specific version of metall run,

```bash
docker pull ghcr.io/autamus/metall:0.13
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/metall metall --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/metall bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the metall container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/metall metall /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC metall container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-metall/).
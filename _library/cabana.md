---
layout: container
name: cabana
github: https://github.com/autamus/registry/blob/main/containers/c/cabana/spack.yaml
versions:
- 0.3.0
- 0.4.0
updated_at: 2021-12-30T15:56:19.082875418Z
size: 53MB
description: 'The Exascale Co-Design Center for Particle Applications Toolkit '
container_url: https://github.com/orgs/autamus/packages/container/package/cabana

---
# cabana
```bash 
Download        : docker pull ghcr.io/autamus/cabana
Compressed Size : 53MB
```

## Description
The Exascale Co-Design Center for Particle Applications Toolkit 

## Usage
### Pull (Download)
To download the latest version of cabana run,

```bash
docker pull ghcr.io/autamus/cabana:latest
```

or to download a specific version of cabana run,

```bash
docker pull ghcr.io/autamus/cabana:0.3.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/cabana cabana --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/cabana bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the cabana container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/cabana cabana /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC cabana container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-cabana/).
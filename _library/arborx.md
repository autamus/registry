---
layout: container
name: arborx
github: https://github.com/autamus/registry/blob/main/containers/a/arborx/spack.yaml
versions:
- "1.0"
- "1.1"
updated_at: 2021-11-04T16:01:29.985907634Z
size: 53MB
description: ArborX is a performance-portable library for geometric search
container_url: https://github.com/orgs/autamus/packages/container/package/arborx

---
# arborx
```bash 
Download        : docker pull ghcr.io/autamus/arborx
Compressed Size : 53MB
```

## Description
ArborX is a performance-portable library for geometric search

## Usage
### Pull (Download)
To download the latest version of arborx run,

```bash
docker pull ghcr.io/autamus/arborx:latest
```

or to download a specific version of arborx run,

```bash
docker pull ghcr.io/autamus/arborx:1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/arborx arborx --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/arborx bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the arborx container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/arborx arborx /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC arborx container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-arborx/).
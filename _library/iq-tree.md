---
layout: container
name: iq-tree
github: https://github.com/autamus/registry/blob/main/containers/i/iq-tree/spack.yaml
versions:
- 2.0.6
- 2.1.3
updated_at: 2021-11-01T15:59:49.303347777Z
size: 53MB
description: IQ-TREE Efficient software for phylogenomic inference
container_url: https://github.com/orgs/autamus/packages/container/package/iq-tree

---
# iq-tree
```bash 
Download        : docker pull ghcr.io/autamus/iq-tree
Compressed Size : 53MB
```

## Description
IQ-TREE Efficient software for phylogenomic inference

## Usage
### Pull (Download)
To download the latest version of iq-tree run,

```bash
docker pull ghcr.io/autamus/iq-tree:latest
```

or to download a specific version of iq-tree run,

```bash
docker pull ghcr.io/autamus/iq-tree:2.0.6
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/iq-tree iq-tree --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/iq-tree bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the iq-tree container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/iq-tree iq-tree /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC iq-tree container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-iq-tree/).
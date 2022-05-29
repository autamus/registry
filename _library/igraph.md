---
layout: container
name: igraph
github: https://github.com/autamus/registry/blob/main/containers/i/igraph/spack.yaml
versions:
- 0.7.1
updated_at: 2022-05-29T18:25:51.383216772Z
size: 34MB
description: igraph is a library for creating and manipulating graphs.
container_url: https://github.com/orgs/autamus/packages/container/package/igraph

---
# igraph
```bash 
Download        : docker pull ghcr.io/autamus/igraph
Compressed Size : 34MB
```

## Description
igraph is a library for creating and manipulating graphs.

## Usage
### Pull (Download)
To download the latest version of igraph run,

```bash
docker pull ghcr.io/autamus/igraph:latest
```

or to download a specific version of igraph run,

```bash
docker pull ghcr.io/autamus/igraph:0.7.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/igraph igraph --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/igraph bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the igraph container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/igraph igraph /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC igraph container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-igraph/).
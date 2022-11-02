---
layout: container
name: graphviz
github: https://github.com/autamus/registry/blob/main/containers/g/graphviz/spack.yaml
versions:
- 2.47.2
- 2.47.3
- 2.48.0
- 2.49.0
- 2.49.2
- 2.49.3
updated_at: 2022-11-02T22:18:10.546101646Z
size: 31MB
description: Graph Visualization Software
container_url: https://github.com/orgs/autamus/packages/container/package/graphviz

---
# graphviz
```bash 
Download        : docker pull ghcr.io/autamus/graphviz
Compressed Size : 31MB
```

## Description
Graph Visualization Software

## Usage
### Pull (Download)
To download the latest version of graphviz run,

```bash
docker pull ghcr.io/autamus/graphviz:latest
```

or to download a specific version of graphviz run,

```bash
docker pull ghcr.io/autamus/graphviz:2.47.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/graphviz graphviz --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/graphviz bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the graphviz container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/graphviz graphviz /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC graphviz container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-graphviz/).
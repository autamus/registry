---
layout: container
name: corset
github: https://github.com/autamus/registry/blob/main/containers/c/corset/spack.yaml
versions:
- "1.06"
- "1.09"
updated_at: 2022-05-29T17:53:54.057137493Z
size: 27MB
description: Corset is a command-line software program to go from a de novo transcriptome
  assembly to gene-level counts.
container_url: https://github.com/orgs/autamus/packages/container/package/corset

---
# corset
```bash 
Download        : docker pull ghcr.io/autamus/corset
Compressed Size : 27MB
```

## Description
Corset is a command-line software program to go from a de novo transcriptome assembly to gene-level counts.

## Usage
### Pull (Download)
To download the latest version of corset run,

```bash
docker pull ghcr.io/autamus/corset:latest
```

or to download a specific version of corset run,

```bash
docker pull ghcr.io/autamus/corset:1.06
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/corset corset --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/corset bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the corset container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/corset corset /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC corset container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-corset/).
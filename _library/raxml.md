---
layout: container
name: raxml
github: https://github.com/autamus/registry/blob/main/containers/r/raxml/spack.yaml
versions:
- 8.2.12
updated_at: 2021-09-17T06:35:52.046692063Z
size: 55MB
description: 'RAxML (Randomized Axelerated Maximum Likelihood) is a program for sequential
  and parallel Maximum Likelihood based inference of large phylogenetic trees. '
container_url: https://github.com/orgs/autamus/packages/container/package/raxml

---
# raxml
```bash 
Download        : docker pull ghcr.io/autamus/raxml
Compressed Size : 55MB
```

## Description
RAxML (Randomized Axelerated Maximum Likelihood) is a program for sequential and parallel Maximum Likelihood based inference of large phylogenetic trees. 

## Usage
### Pull (Download)
To download the latest version of raxml run,

```bash
docker pull ghcr.io/autamus/raxml:latest
```

or to download a specific version of raxml run,

```bash
docker pull ghcr.io/autamus/raxml:8.2.12
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/raxml raxml --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/raxml bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the raxml container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/raxml raxml /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC raxml container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-raxml/).
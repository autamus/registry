---
layout: container
name: diamond
github: https://github.com/autamus/registry/blob/main/containers/d/diamond/spack.yaml
versions:
- 2.0.10
- 2.0.11
- 2.0.12
- 2.0.13
- 2.0.4
- 2.0.8
- 2.0.9
updated_at: 2021-10-26T04:22:29.767910478Z
size: 29MB
description: DIAMOND is a sequence aligner for protein and translated DNA searches,
  designed for high performance analysis of big sequence data.
container_url: https://github.com/orgs/autamus/packages/container/package/diamond

---
# diamond
```bash 
Download        : docker pull ghcr.io/autamus/diamond
Compressed Size : 29MB
```

## Description
DIAMOND is a sequence aligner for protein and translated DNA searches, designed for high performance analysis of big sequence data.

## Usage
### Pull (Download)
To download the latest version of diamond run,

```bash
docker pull ghcr.io/autamus/diamond:latest
```

or to download a specific version of diamond run,

```bash
docker pull ghcr.io/autamus/diamond:2.0.10
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/diamond diamond --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/diamond bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the diamond container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/diamond diamond /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC diamond container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-diamond/).
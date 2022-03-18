---
layout: container
name: mothur
github: https://github.com/autamus/registry/blob/main/containers/m/mothur/spack.yaml
versions:
- 1.43.0
- 1.44.3
- 1.45.1
- 1.45.3
- 1.46.0
- 1.46.1
updated_at: 2022-03-18T18:19:26.900433075Z
size: 73MB
description: This project seeks to develop a single piece of open-source, expandable
  software to fill the bioinformatics needs of the microbial ecology community.
container_url: https://github.com/orgs/autamus/packages/container/package/mothur

---
# mothur
```bash 
Download        : docker pull ghcr.io/autamus/mothur
Compressed Size : 73MB
```

## Description
This project seeks to develop a single piece of open-source, expandable software to fill the bioinformatics needs of the microbial ecology community.

## Usage
### Pull (Download)
To download the latest version of mothur run,

```bash
docker pull ghcr.io/autamus/mothur:latest
```

or to download a specific version of mothur run,

```bash
docker pull ghcr.io/autamus/mothur:1.43.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/mothur mothur --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/mothur bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the mothur container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/mothur mothur /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC mothur container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-mothur/).
---
layout: container
name: plink
github: https://github.com/autamus/registry/blob/main/containers/p/plink/spack.yaml
versions:
- 1.9.beta.6.10
updated_at: 2021-05-26T06:54:09.318209501Z
size: 30MB
description: PLINK is a free, open-source whole genome association analysis toolset,
  designed to perform a range of basic, large-scale analyses in a computationally
  efficient manner.
container_url: https://github.com/orgs/autamus/packages/container/package/plink

---
# plink
```bash 
Download        : docker pull ghcr.io/autamus/plink
Compressed Size : 30MB
```

## Description
PLINK is a free, open-source whole genome association analysis toolset, designed to perform a range of basic, large-scale analyses in a computationally efficient manner.

## Usage
### Pull (Download)
To download the latest version of plink run,

```bash
docker pull ghcr.io/autamus/plink:latest
```

or to download a specific version of plink run,

```bash
docker pull ghcr.io/autamus/plink:1.9.beta.6.10
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/plink plink --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/plink bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the plink container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/plink plink /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC plink container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-plink/).
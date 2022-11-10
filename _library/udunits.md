---
layout: container
name: udunits
github: https://github.com/autamus/registry/blob/main/containers/u/udunits/spack.yaml
versions:
- 2.2.28
updated_at: 2022-11-10T17:44:27.078705011Z
size: 27MB
description: Automated units conversion
container_url: https://github.com/orgs/autamus/packages/container/package/udunits

---
# udunits
```bash 
Download        : docker pull ghcr.io/autamus/udunits
Compressed Size : 27MB
```

## Description
Automated units conversion

## Usage
### Pull (Download)
To download the latest version of udunits run,

```bash
docker pull ghcr.io/autamus/udunits:latest
```

or to download a specific version of udunits run,

```bash
docker pull ghcr.io/autamus/udunits:2.2.28
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/udunits udunits --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/udunits bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the udunits container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/udunits udunits /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC udunits container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-udunits/).
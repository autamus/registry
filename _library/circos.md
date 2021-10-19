---
layout: container
name: circos
github: https://github.com/autamus/registry/blob/main/containers/c/circos/spack.yaml
versions:
- 0.69.6
updated_at: 2021-10-19T07:24:32.644331731Z
size: 126MB
description: Circos is a software package for visualizing data and information.
container_url: https://github.com/orgs/autamus/packages/container/package/circos

---
# circos
```bash 
Download        : docker pull ghcr.io/autamus/circos
Compressed Size : 126MB
```

## Description
Circos is a software package for visualizing data and information.

## Usage
### Pull (Download)
To download the latest version of circos run,

```bash
docker pull ghcr.io/autamus/circos:latest
```

or to download a specific version of circos run,

```bash
docker pull ghcr.io/autamus/circos:0.69.6
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/circos circos --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/circos bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the circos container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/circos circos /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC circos container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-circos/).
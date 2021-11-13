---
layout: container
name: jasper
github: https://github.com/autamus/registry/blob/main/containers/j/jasper/spack.yaml
versions:
- 2.0.32
- 2.0.33
- "20210822.2247"
updated_at: 2021-11-13T18:53:06.522103914Z
size: 28MB
description: Library for manipulating JPEG-2000 images
container_url: https://github.com/orgs/autamus/packages/container/package/jasper

---
# jasper
```bash 
Download        : docker pull ghcr.io/autamus/jasper
Compressed Size : 28MB
```

## Description
Library for manipulating JPEG-2000 images

## Usage
### Pull (Download)
To download the latest version of jasper run,

```bash
docker pull ghcr.io/autamus/jasper:latest
```

or to download a specific version of jasper run,

```bash
docker pull ghcr.io/autamus/jasper:2.0.32
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/jasper jasper --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/jasper bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the jasper container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/jasper jasper /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC jasper container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-jasper/).
---
layout: container
name: alps
github: https://github.com/autamus/registry/blob/main/containers/a/alps/spack.yaml
versions:
- 2.3.0
updated_at: 2022-01-09T16:19:02.308193589Z
size: 260MB
description: 'Algorithms for Physics Simulations Tags: Condensed Matter Physics, Computational
  Physics '
container_url: https://github.com/orgs/autamus/packages/container/package/alps

---
# alps
```bash 
Download        : docker pull ghcr.io/autamus/alps
Compressed Size : 260MB
```

## Description
Algorithms for Physics Simulations Tags: Condensed Matter Physics, Computational Physics 

## Usage
### Pull (Download)
To download the latest version of alps run,

```bash
docker pull ghcr.io/autamus/alps:latest
```

or to download a specific version of alps run,

```bash
docker pull ghcr.io/autamus/alps:2.3.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/alps alps --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/alps bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the alps container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/alps alps /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC alps container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-alps/).
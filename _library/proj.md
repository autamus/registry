---
layout: container
name: proj
github: https://github.com/autamus/registry/blob/main/containers/p/proj/spack.yaml
versions:
- 7.2.1
- 8.1.0
- 8.2.1
updated_at: 2022-11-02T23:22:50.657220531Z
size: 44MB
description: PROJ is a generic coordinate transformation software, that transforms
  geospatial coordinates from one coordinate reference system (CRS) to another. This
  includes cartographic projections as well as geodetic transformations.
container_url: https://github.com/orgs/autamus/packages/container/package/proj

---
# proj
```bash 
Download        : docker pull ghcr.io/autamus/proj
Compressed Size : 44MB
```

## Description
PROJ is a generic coordinate transformation software, that transforms geospatial coordinates from one coordinate reference system (CRS) to another. This includes cartographic projections as well as geodetic transformations.

## Usage
### Pull (Download)
To download the latest version of proj run,

```bash
docker pull ghcr.io/autamus/proj:latest
```

or to download a specific version of proj run,

```bash
docker pull ghcr.io/autamus/proj:7.2.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/proj proj --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/proj bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the proj container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/proj proj /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC proj container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-proj/).
---
layout: container
name: grass
github: https://github.com/autamus/registry/blob/main/containers/g/grass/spack.yaml
versions:
- 7.8.2
- 7.8.5
- 7.8.6
updated_at: 2021-10-19T07:32:33.367243016Z
size: 149MB
description: GRASS GIS (Geographic Resources Analysis Support System), is a free and
  open source Geographic Information System (GIS) software suite used for geospatial
  data management and analysis, image processing, graphics and maps production, spatial
  modeling, and visualization.
container_url: https://github.com/orgs/autamus/packages/container/package/grass

---
# grass
```bash 
Download        : docker pull ghcr.io/autamus/grass
Compressed Size : 149MB
```

## Description
GRASS GIS (Geographic Resources Analysis Support System), is a free and open source Geographic Information System (GIS) software suite used for geospatial data management and analysis, image processing, graphics and maps production, spatial modeling, and visualization.

## Usage
### Pull (Download)
To download the latest version of grass run,

```bash
docker pull ghcr.io/autamus/grass:latest
```

or to download a specific version of grass run,

```bash
docker pull ghcr.io/autamus/grass:7.8.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/grass grass --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/grass bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the grass container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/grass grass /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC grass container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-grass/).
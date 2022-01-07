---
layout: container
name: gdal
github: https://github.com/autamus/registry/blob/main/containers/g/gdal/spack.yaml
versions:
- 3.3.0
- 3.3.1
- 3.3.2
- 3.3.3
- 3.4.0
- 3.4.1
updated_at: 2022-01-07T16:10:12.39589724Z
size: 56MB
description: 'GDAL (Geospatial Data Abstraction Library) is a translator library for
  raster and vector geospatial data formats that is released under an X/MIT style
  Open Source license by the Open Source Geospatial Foundation. As a library, it presents
  a single raster abstract data model and vector abstract data model to the calling
  application for all supported formats. It also comes with a variety of useful command
  line utilities for data translation and processing. '
container_url: https://github.com/orgs/autamus/packages/container/package/gdal

---
# gdal
```bash 
Download        : docker pull ghcr.io/autamus/gdal
Compressed Size : 56MB
```

## Description
GDAL (Geospatial Data Abstraction Library) is a translator library for raster and vector geospatial data formats that is released under an X/MIT style Open Source license by the Open Source Geospatial Foundation. As a library, it presents a single raster abstract data model and vector abstract data model to the calling application for all supported formats. It also comes with a variety of useful command line utilities for data translation and processing. 

## Usage
### Pull (Download)
To download the latest version of gdal run,

```bash
docker pull ghcr.io/autamus/gdal:latest
```

or to download a specific version of gdal run,

```bash
docker pull ghcr.io/autamus/gdal:3.3.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/gdal gdal --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/gdal bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the gdal container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/gdal gdal /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC gdal container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-gdal/).
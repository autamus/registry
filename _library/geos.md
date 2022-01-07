---
layout: container
name: geos
github: https://github.com/autamus/registry/blob/main/containers/g/geos/spack.yaml
versions:
- 3.8.1
- 3.9.1
updated_at: 2022-01-07T16:12:05.80575729Z
size: 28MB
description: GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology
  Suite (JTS). As such, it aims to contain the complete functionality of JTS in C++.
  This includes all the OpenGIS Simple Features for SQL spatial predicate functions
  and spatial operators, as well as specific JTS enhanced topology functions.
container_url: https://github.com/orgs/autamus/packages/container/package/geos

---
# geos
```bash 
Download        : docker pull ghcr.io/autamus/geos
Compressed Size : 28MB
```

## Description
GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology Suite (JTS). As such, it aims to contain the complete functionality of JTS in C++. This includes all the OpenGIS Simple Features for SQL spatial predicate functions and spatial operators, as well as specific JTS enhanced topology functions.

## Usage
### Pull (Download)
To download the latest version of geos run,

```bash
docker pull ghcr.io/autamus/geos:latest
```

or to download a specific version of geos run,

```bash
docker pull ghcr.io/autamus/geos:3.8.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/geos geos --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/geos bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the geos container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/geos geos /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC geos container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-geos/).
---
layout: container
name: gasnet
github: https://github.com/autamus/registry/blob/main/containers/g/gasnet/spack.yaml
versions:
- 2021.3.0
- 2021.9.0
- 2022.3.0
- 2022.9.0
updated_at: 2022-10-14T15:22:17.41420017Z
size: 30MB
description: 'GASNet is a language-independent, networking middleware layer that provides
  network-independent, high-performance communication primitives including Remote
  Memory Access (RMA) and Active Messages (AM). It has been used to implement parallel
  programming models and libraries such as UPC, UPC++, Co-Array Fortran, Legion, Chapel,
  and many others. The interface is primarily intended as a compilation target and
  for use by runtime library writers (as opposed to end users), and the primary goals
  are high performance, interface portability, and expressiveness. ***NOTICE***: The
  GASNet library built by this Spack package is ONLY intended for unit-testing purposes,
  and is generally UNSUITABLE FOR PRODUCTION USE. The RECOMMENDED way to build GASNet
  is as an embedded library as configured by the higher-level client runtime package
  (UPC++, Legion, etc), including system-specific configuration. '
container_url: https://github.com/orgs/autamus/packages/container/package/gasnet

---
# gasnet
```bash 
Download        : docker pull ghcr.io/autamus/gasnet
Compressed Size : 30MB
```

## Description
GASNet is a language-independent, networking middleware layer that provides network-independent, high-performance communication primitives including Remote Memory Access (RMA) and Active Messages (AM). It has been used to implement parallel programming models and libraries such as UPC, UPC++, Co-Array Fortran, Legion, Chapel, and many others. The interface is primarily intended as a compilation target and for use by runtime library writers (as opposed to end users), and the primary goals are high performance, interface portability, and expressiveness. ***NOTICE***: The GASNet library built by this Spack package is ONLY intended for unit-testing purposes, and is generally UNSUITABLE FOR PRODUCTION USE. The RECOMMENDED way to build GASNet is as an embedded library as configured by the higher-level client runtime package (UPC++, Legion, etc), including system-specific configuration. 

## Usage
### Pull (Download)
To download the latest version of gasnet run,

```bash
docker pull ghcr.io/autamus/gasnet:latest
```

or to download a specific version of gasnet run,

```bash
docker pull ghcr.io/autamus/gasnet:2021.3.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/gasnet gasnet --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/gasnet bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the gasnet container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/gasnet gasnet /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC gasnet container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-gasnet/).
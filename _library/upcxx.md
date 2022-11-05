---
layout: container
name: upcxx
github: https://github.com/autamus/registry/blob/main/containers/u/upcxx/spack.yaml
versions:
- 2021.3.0
- 2021.9.0
- 2022.9.0
updated_at: 2022-11-05T22:50:55.622921291Z
size: 97MB
description: UPC++ is a C++ library that supports Partitioned Global Address Space
  (PGAS) programming, and is designed to interoperate smoothly and efficiently with
  MPI, OpenMP, CUDA and AMTs. It leverages GASNet-EX to deliver low-overhead, fine-grained
  communication, including Remote Memory Access (RMA) and Remote Procedure Call (RPC).
container_url: https://github.com/orgs/autamus/packages/container/package/upcxx

---
# upcxx
```bash 
Download        : docker pull ghcr.io/autamus/upcxx
Compressed Size : 97MB
```

## Description
UPC++ is a C++ library that supports Partitioned Global Address Space (PGAS) programming, and is designed to interoperate smoothly and efficiently with MPI, OpenMP, CUDA and AMTs. It leverages GASNet-EX to deliver low-overhead, fine-grained communication, including Remote Memory Access (RMA) and Remote Procedure Call (RPC).

## Usage
### Pull (Download)
To download the latest version of upcxx run,

```bash
docker pull ghcr.io/autamus/upcxx:latest
```

or to download a specific version of upcxx run,

```bash
docker pull ghcr.io/autamus/upcxx:2021.3.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/upcxx upcxx --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/upcxx bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the upcxx container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/upcxx upcxx /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC upcxx container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-upcxx/).
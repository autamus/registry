---
layout: container
name: bolt
github: https://github.com/autamus/registry/blob/main/containers/b/bolt/spack.yaml
versions:
- "2.0"
updated_at: 2022-11-02T21:03:52.66564035Z
size: 27MB
description: BOLT targets a high-performing OpenMP implementation, especially specialized
  for fine-grain parallelism. Unlike other OpenMP implementations, BOLT utilizes a
  lightweight threading model for its underlying threading mechanism. It currently
  adopts Argobots, a new holistic, low-level threading and tasking runtime, in order
  to overcome shortcomings of conventional OS-level threads. The current BOLT implementation
  is based on the OpenMP runtime in LLVM, and thus it can be used with LLVM/Clang,
  Intel OpenMP compiler, and GCC.
container_url: https://github.com/orgs/autamus/packages/container/package/bolt

---
# bolt
```bash 
Download        : docker pull ghcr.io/autamus/bolt
Compressed Size : 27MB
```

## Description
BOLT targets a high-performing OpenMP implementation, especially specialized for fine-grain parallelism. Unlike other OpenMP implementations, BOLT utilizes a lightweight threading model for its underlying threading mechanism. It currently adopts Argobots, a new holistic, low-level threading and tasking runtime, in order to overcome shortcomings of conventional OS-level threads. The current BOLT implementation is based on the OpenMP runtime in LLVM, and thus it can be used with LLVM/Clang, Intel OpenMP compiler, and GCC.

## Usage
### Pull (Download)
To download the latest version of bolt run,

```bash
docker pull ghcr.io/autamus/bolt:latest
```

or to download a specific version of bolt run,

```bash
docker pull ghcr.io/autamus/bolt:2.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/bolt bolt --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/bolt bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the bolt container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/bolt bolt /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC bolt container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-bolt/).
---
layout: container
name: unifyfs
github: https://github.com/autamus/registry/blob/main/containers/u/unifyfs/spack.yaml
versions:
- 0.9.2
updated_at: 2021-10-30T15:29:28.132260446Z
size: 79MB
description: User level file system that enables applications to use node-local storage
  as burst buffers for shared files. Supports scalable and efficient aggregation of
  I/O bandwidth from burst buffers while having the same life cycle as a batch-submitted
  job. UnifyFS is designed to support common I/O workloads, including checkpoint/restart.
  While primarily designed for N-N write/read, UnifyFS compliments its functionality
  with the support for N-1 write/read.
container_url: https://github.com/orgs/autamus/packages/container/package/unifyfs

---
# unifyfs
```bash 
Download        : docker pull ghcr.io/autamus/unifyfs
Compressed Size : 79MB
```

## Description
User level file system that enables applications to use node-local storage as burst buffers for shared files. Supports scalable and efficient aggregation of I/O bandwidth from burst buffers while having the same life cycle as a batch-submitted job. UnifyFS is designed to support common I/O workloads, including checkpoint/restart. While primarily designed for N-N write/read, UnifyFS compliments its functionality with the support for N-1 write/read.

## Usage
### Pull (Download)
To download the latest version of unifyfs run,

```bash
docker pull ghcr.io/autamus/unifyfs:latest
```

or to download a specific version of unifyfs run,

```bash
docker pull ghcr.io/autamus/unifyfs:0.9.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/unifyfs unifyfs --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/unifyfs bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the unifyfs container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/unifyfs unifyfs /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC unifyfs container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-unifyfs/).
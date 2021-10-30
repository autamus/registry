---
layout: container
name: pumi
github: https://github.com/autamus/registry/blob/main/containers/p/pumi/spack.yaml
versions:
- 2.2.5
- 2.2.6
updated_at: 2021-10-30T15:22:13.264569386Z
size: 76MB
description: SCOREC RPI's Parallel Unstructured Mesh Infrastructure (PUMI). An efficient
  distributed mesh data structure and methods to support parallel adaptive analysis
  including general mesh-based operations, such as mesh entity creation/deletion,
  adjacency and geometric classification, iterators, arbitrary (field) data attachable
  to mesh entities, efficient communication involving entities duplicated across multiple
  tasks, migration of mesh entities between tasks, and dynamic load balancing.
container_url: https://github.com/orgs/autamus/packages/container/package/pumi

---
# pumi
```bash 
Download        : docker pull ghcr.io/autamus/pumi
Compressed Size : 76MB
```

## Description
SCOREC RPI's Parallel Unstructured Mesh Infrastructure (PUMI). An efficient distributed mesh data structure and methods to support parallel adaptive analysis including general mesh-based operations, such as mesh entity creation/deletion, adjacency and geometric classification, iterators, arbitrary (field) data attachable to mesh entities, efficient communication involving entities duplicated across multiple tasks, migration of mesh entities between tasks, and dynamic load balancing.

## Usage
### Pull (Download)
To download the latest version of pumi run,

```bash
docker pull ghcr.io/autamus/pumi:latest
```

or to download a specific version of pumi run,

```bash
docker pull ghcr.io/autamus/pumi:2.2.5
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/pumi pumi --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/pumi bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the pumi container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/pumi pumi /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC pumi container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-pumi/).
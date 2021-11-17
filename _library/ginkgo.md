---
layout: container
name: ginkgo
github: https://github.com/autamus/registry/blob/main/containers/g/ginkgo/spack.yaml
versions:
- 1.3.0
- 1.4.0
updated_at: 2021-11-17T15:54:37.531489362Z
size: 32MB
description: High-performance linear algebra library for manycore systems, with a
  focus on sparse solution of linear systems.
container_url: https://github.com/orgs/autamus/packages/container/package/ginkgo

---
# ginkgo
```bash 
Download        : docker pull ghcr.io/autamus/ginkgo
Compressed Size : 32MB
```

## Description
High-performance linear algebra library for manycore systems, with a focus on sparse solution of linear systems.

## Usage
### Pull (Download)
To download the latest version of ginkgo run,

```bash
docker pull ghcr.io/autamus/ginkgo:latest
```

or to download a specific version of ginkgo run,

```bash
docker pull ghcr.io/autamus/ginkgo:1.3.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/ginkgo ginkgo --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/ginkgo bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the ginkgo container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/ginkgo ginkgo /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC ginkgo container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-ginkgo/).
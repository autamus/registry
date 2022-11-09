---
layout: container
name: hypre
github: https://github.com/autamus/registry/blob/main/containers/h/hypre/spack.yaml
versions:
- 2.21.0
- 2.22.0
- 2.22.1
- 2.23.0
- 2.26.0
updated_at: 2022-11-09T21:53:52.046131119Z
size: 89MB
description: Hypre is a library of high performance preconditioners that features
  parallel multigrid methods for both structured and unstructured grid problems.
container_url: https://github.com/orgs/autamus/packages/container/package/hypre

---
# hypre
```bash 
Download        : docker pull ghcr.io/autamus/hypre
Compressed Size : 89MB
```

## Description
Hypre is a library of high performance preconditioners that features parallel multigrid methods for both structured and unstructured grid problems.

## Usage
### Pull (Download)
To download the latest version of hypre run,

```bash
docker pull ghcr.io/autamus/hypre:latest
```

or to download a specific version of hypre run,

```bash
docker pull ghcr.io/autamus/hypre:2.21.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/hypre hypre --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/hypre bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the hypre container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/hypre hypre /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC hypre container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-hypre/).
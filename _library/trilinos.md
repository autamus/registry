---
layout: container
name: trilinos
github: https://github.com/autamus/registry/blob/main/containers/t/trilinos/spack.yaml
versions:
- 13.0.1
- 13.2.0
updated_at: 2021-11-04T16:02:15.040580754Z
size: 108MB
description: 'The Trilinos Project is an effort to develop algorithms and enabling
  technologies within an object-oriented software framework for the solution of large-scale,
  complex multi-physics engineering and scientific problems. A unique design feature
  of Trilinos is its focus on packages. '
container_url: https://github.com/orgs/autamus/packages/container/package/trilinos

---
# trilinos
```bash 
Download        : docker pull ghcr.io/autamus/trilinos
Compressed Size : 108MB
```

## Description
The Trilinos Project is an effort to develop algorithms and enabling technologies within an object-oriented software framework for the solution of large-scale, complex multi-physics engineering and scientific problems. A unique design feature of Trilinos is its focus on packages. 

## Usage
### Pull (Download)
To download the latest version of trilinos run,

```bash
docker pull ghcr.io/autamus/trilinos:latest
```

or to download a specific version of trilinos run,

```bash
docker pull ghcr.io/autamus/trilinos:13.0.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/trilinos trilinos --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/trilinos bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the trilinos container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/trilinos trilinos /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC trilinos container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-trilinos/).
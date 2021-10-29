---
layout: container
name: glpk
github: https://github.com/autamus/registry/blob/main/containers/g/glpk/spack.yaml
versions:
- "4.65"
updated_at: 2021-10-29T14:56:24.915904855Z
size: 27MB
description: 'The GLPK (GNU Linear Programming Kit) package is intended for solving
  large-scale linear programming (LP), mixed integer programming (MIP), and other
  related problems. It is a set of routines written in ANSI C and organized in the
  form of a callable library. '
container_url: https://github.com/orgs/autamus/packages/container/package/glpk

---
# glpk
```bash 
Download        : docker pull ghcr.io/autamus/glpk
Compressed Size : 27MB
```

## Description
The GLPK (GNU Linear Programming Kit) package is intended for solving large-scale linear programming (LP), mixed integer programming (MIP), and other related problems. It is a set of routines written in ANSI C and organized in the form of a callable library. 

## Usage
### Pull (Download)
To download the latest version of glpk run,

```bash
docker pull ghcr.io/autamus/glpk:latest
```

or to download a specific version of glpk run,

```bash
docker pull ghcr.io/autamus/glpk:4.65
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/glpk glpk --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/glpk bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the glpk container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/glpk glpk /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC glpk container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-glpk/).
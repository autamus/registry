---
layout: container
name: lp-solve
github: https://github.com/autamus/registry/blob/main/containers/l/lp-solve/spack.yaml
versions:
- 5.5.2.11
updated_at: 2022-08-01T19:02:33.295230505Z
size: 28MB
description: lp_solve is a Mixed Integer Linear Programming (MILP) solver.
container_url: https://github.com/orgs/autamus/packages/container/package/lp-solve

---
# lp-solve
```bash 
Download        : docker pull ghcr.io/autamus/lp-solve
Compressed Size : 28MB
```

## Description
lp_solve is a Mixed Integer Linear Programming (MILP) solver.

## Usage
### Pull (Download)
To download the latest version of lp-solve run,

```bash
docker pull ghcr.io/autamus/lp-solve:latest
```

or to download a specific version of lp-solve run,

```bash
docker pull ghcr.io/autamus/lp-solve:5.5.2.11
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/lp-solve lp-solve --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/lp-solve bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the lp-solve container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/lp-solve lp-solve /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC lp-solve container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-lp-solve/).
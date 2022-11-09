---
layout: container
name: slate
github: https://github.com/autamus/registry/blob/main/containers/s/slate/spack.yaml
versions:
- 2021.05.02
- 2022.07.00
updated_at: 2022-11-09T23:34:28.533216844Z
size: 113MB
description: The Software for Linear Algebra Targeting Exascale (SLATE) project is
  to provide fundamental dense linear algebra capabilities to the US Department of
  Energy and to the high-performance computing (HPC) community at large. To this end,
  SLATE will provide basic dense matrix operations (e.g., matrix multiplication, rank-k
  update, triangular solve), linear systems solvers, least square solvers, singular
  value and eigenvalue solvers.
container_url: https://github.com/orgs/autamus/packages/container/package/slate

---
# slate
```bash 
Download        : docker pull ghcr.io/autamus/slate
Compressed Size : 113MB
```

## Description
The Software for Linear Algebra Targeting Exascale (SLATE) project is to provide fundamental dense linear algebra capabilities to the US Department of Energy and to the high-performance computing (HPC) community at large. To this end, SLATE will provide basic dense matrix operations (e.g., matrix multiplication, rank-k update, triangular solve), linear systems solvers, least square solvers, singular value and eigenvalue solvers.

## Usage
### Pull (Download)
To download the latest version of slate run,

```bash
docker pull ghcr.io/autamus/slate:latest
```

or to download a specific version of slate run,

```bash
docker pull ghcr.io/autamus/slate:2021.05.02
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/slate slate --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/slate bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the slate container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/slate slate /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC slate container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-slate/).
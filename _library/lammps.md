---
layout: container
name: lammps
github: https://github.com/autamus/registry/blob/main/containers/l/lammps/spack.yaml
versions:
- "20210310"
updated_at: 2022-01-07T16:16:46.587521428Z
size: 91MB
description: 'LAMMPS stands for Large-scale Atomic/Molecular Massively Parallel Simulator.
  This package uses patch releases, not stable release. See https://github.com/spack/spack/pull/5342
  for a detailed discussion. '
container_url: https://github.com/orgs/autamus/packages/container/package/lammps

---
# lammps
```bash 
Download        : docker pull ghcr.io/autamus/lammps
Compressed Size : 91MB
```

## Description
LAMMPS stands for Large-scale Atomic/Molecular Massively Parallel Simulator. This package uses patch releases, not stable release. See https://github.com/spack/spack/pull/5342 for a detailed discussion. 

## Usage
### Pull (Download)
To download the latest version of lammps run,

```bash
docker pull ghcr.io/autamus/lammps:latest
```

or to download a specific version of lammps run,

```bash
docker pull ghcr.io/autamus/lammps:20210310
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/lammps lammps --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/lammps bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the lammps container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/lammps lammps /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC lammps container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-lammps/).
---
layout: container
name: cantera
github: https://github.com/autamus/registry/blob/main/containers/c/cantera/spack.yaml
versions:
- 2.4.0
- 2.5.1
updated_at: 2021-11-12T16:04:59.85819762Z
size: 127MB
description: Cantera is a suite of object-oriented software tools for problems involving
  chemical kinetics, thermodynamics, and/or transport processes.
container_url: https://github.com/orgs/autamus/packages/container/package/cantera

---
# cantera
```bash 
Download        : docker pull ghcr.io/autamus/cantera
Compressed Size : 127MB
```

## Description
Cantera is a suite of object-oriented software tools for problems involving chemical kinetics, thermodynamics, and/or transport processes.

## Usage
### Pull (Download)
To download the latest version of cantera run,

```bash
docker pull ghcr.io/autamus/cantera:latest
```

or to download a specific version of cantera run,

```bash
docker pull ghcr.io/autamus/cantera:2.4.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/cantera cantera --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/cantera bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the cantera container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/cantera cantera /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC cantera container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-cantera/).
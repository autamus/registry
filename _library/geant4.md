---
layout: container
name: geant4
github: https://github.com/autamus/registry/blob/main/containers/g/geant4/spack.yaml
versions:
- 10.7.1
- 10.7.2
updated_at: 2021-11-17T16:04:27.872800255Z
size: 1139MB
description: Geant4 is a toolkit for the simulation of the passage of particles through
  matter. Its areas of application include high energy, nuclear and accelerator physics,
  as well as studies in medical and space science.
container_url: https://github.com/orgs/autamus/packages/container/package/geant4

---
# geant4
```bash 
Download        : docker pull ghcr.io/autamus/geant4
Compressed Size : 1139MB
```

## Description
Geant4 is a toolkit for the simulation of the passage of particles through matter. Its areas of application include high energy, nuclear and accelerator physics, as well as studies in medical and space science.

## Usage
### Pull (Download)
To download the latest version of geant4 run,

```bash
docker pull ghcr.io/autamus/geant4:latest
```

or to download a specific version of geant4 run,

```bash
docker pull ghcr.io/autamus/geant4:10.7.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/geant4 geant4 --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/geant4 bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the geant4 container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/geant4 geant4 /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC geant4 container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-geant4/).
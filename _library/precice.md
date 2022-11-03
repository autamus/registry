---
layout: container
name: precice
github: https://github.com/autamus/registry/blob/main/containers/p/precice/spack.yaml
versions:
- 2.2.1
- 2.3.0
- 2.5.0
updated_at: 2022-11-03T00:12:01.089973655Z
size: 171MB
description: preCICE (Precise Code Interaction Coupling Environment) is a coupling
  library for partitioned multi-physics simulations. Partitioned means that preCICE
  couples existing programs (solvers) capable of simulating a subpart of the complete
  physics involved in a simulation.
container_url: https://github.com/orgs/autamus/packages/container/package/precice

---
# precice
```bash 
Download        : docker pull ghcr.io/autamus/precice
Compressed Size : 171MB
```

## Description
preCICE (Precise Code Interaction Coupling Environment) is a coupling library for partitioned multi-physics simulations. Partitioned means that preCICE couples existing programs (solvers) capable of simulating a subpart of the complete physics involved in a simulation.

## Usage
### Pull (Download)
To download the latest version of precice run,

```bash
docker pull ghcr.io/autamus/precice:latest
```

or to download a specific version of precice run,

```bash
docker pull ghcr.io/autamus/precice:2.2.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/precice precice --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/precice bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the precice container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/precice precice /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC precice container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-precice/).
---
layout: container
name: ascent
github: https://github.com/autamus/registry/blob/main/containers/a/ascent/spack.yaml
versions:
- 0.6.0
- 0.7.0
- 0.7.1
updated_at: 2021-11-03T15:45:56.879650146Z
size: 114MB
description: Ascent is an open source many-core capable lightweight in situ visualization
  and analysis infrastructure for multi-physics HPC simulations.
container_url: https://github.com/orgs/autamus/packages/container/package/ascent

---
# ascent
```bash 
Download        : docker pull ghcr.io/autamus/ascent
Compressed Size : 114MB
```

## Description
Ascent is an open source many-core capable lightweight in situ visualization and analysis infrastructure for multi-physics HPC simulations.

## Usage
### Pull (Download)
To download the latest version of ascent run,

```bash
docker pull ghcr.io/autamus/ascent:latest
```

or to download a specific version of ascent run,

```bash
docker pull ghcr.io/autamus/ascent:0.6.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/ascent ascent --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/ascent bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the ascent container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/ascent ascent /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC ascent container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-ascent/).
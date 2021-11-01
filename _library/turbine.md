---
layout: container
name: turbine
github: https://github.com/autamus/registry/blob/main/containers/t/turbine/spack.yaml
versions:
- 1.3.0
updated_at: 2021-11-01T16:16:51.287099405Z
size: 71MB
description: 'Turbine: The Swift/T runtime'
container_url: https://github.com/orgs/autamus/packages/container/package/turbine

---
# turbine
```bash 
Download        : docker pull ghcr.io/autamus/turbine
Compressed Size : 71MB
```

## Description
Turbine: The Swift/T runtime

## Usage
### Pull (Download)
To download the latest version of turbine run,

```bash
docker pull ghcr.io/autamus/turbine:latest
```

or to download a specific version of turbine run,

```bash
docker pull ghcr.io/autamus/turbine:1.3.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/turbine turbine --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/turbine bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the turbine container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/turbine turbine /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC turbine container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-turbine/).
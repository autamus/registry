---
layout: container
name: tasmanian
github: https://github.com/autamus/registry/blob/main/containers/t/tasmanian/spack.yaml
versions:
- "7.5"
- "7.7"
updated_at: 2021-10-27T18:19:04.55627607Z
size: 55MB
description: The Toolkit for Adaptive Stochastic Modeling and Non-Intrusive ApproximatioN
  is a robust library for high dimensional integration and interpolation as well as
  parameter calibration.
container_url: https://github.com/orgs/autamus/packages/container/package/tasmanian

---
# tasmanian
```bash 
Download        : docker pull ghcr.io/autamus/tasmanian
Compressed Size : 55MB
```

## Description
The Toolkit for Adaptive Stochastic Modeling and Non-Intrusive ApproximatioN is a robust library for high dimensional integration and interpolation as well as parameter calibration.

## Usage
### Pull (Download)
To download the latest version of tasmanian run,

```bash
docker pull ghcr.io/autamus/tasmanian:latest
```

or to download a specific version of tasmanian run,

```bash
docker pull ghcr.io/autamus/tasmanian:7.5
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/tasmanian tasmanian --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/tasmanian bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the tasmanian container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/tasmanian tasmanian /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC tasmanian container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-tasmanian/).
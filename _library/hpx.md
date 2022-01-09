---
layout: container
name: hpx
github: https://github.com/autamus/registry/blob/main/containers/h/hpx/spack.yaml
versions:
- 1.6.0
- 1.7.0
- 1.7.1
updated_at: 2022-01-09T16:26:02.238118128Z
size: 123MB
description: C++ runtime system for parallel and distributed applications.
container_url: https://github.com/orgs/autamus/packages/container/package/hpx

---
# hpx
```bash 
Download        : docker pull ghcr.io/autamus/hpx
Compressed Size : 123MB
```

## Description
C++ runtime system for parallel and distributed applications.

## Usage
### Pull (Download)
To download the latest version of hpx run,

```bash
docker pull ghcr.io/autamus/hpx:latest
```

or to download a specific version of hpx run,

```bash
docker pull ghcr.io/autamus/hpx:1.6.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/hpx hpx --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/hpx bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the hpx container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/hpx hpx /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC hpx container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-hpx/).
---
layout: container
name: aria2
github: https://github.com/autamus/registry/blob/main/containers/a/aria2/spack.yaml
versions:
- 1.35.0
- 1.36.0
updated_at: 2022-01-09T16:14:53.667000954Z
size: 43MB
description: An ultra fast download utility
container_url: https://github.com/orgs/autamus/packages/container/package/aria2

---
# aria2
```bash 
Download        : docker pull ghcr.io/autamus/aria2
Compressed Size : 43MB
```

## Description
An ultra fast download utility

## Usage
### Pull (Download)
To download the latest version of aria2 run,

```bash
docker pull ghcr.io/autamus/aria2:latest
```

or to download a specific version of aria2 run,

```bash
docker pull ghcr.io/autamus/aria2:1.35.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/aria2 aria2 --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/aria2 bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the aria2 container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/aria2 aria2 /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC aria2 container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-aria2/).
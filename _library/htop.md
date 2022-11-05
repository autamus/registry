---
layout: container
name: htop
github: https://github.com/autamus/registry/blob/main/containers/h/htop/spack.yaml
versions:
- 2.2.0
- 3.1.1
- 3.2.0
updated_at: 2022-11-05T21:13:27.052408314Z
size: 29MB
description: htop is an interactive text-mode process viewer for Unix systems.
container_url: https://github.com/orgs/autamus/packages/container/package/htop

---
# htop
```bash 
Download        : docker pull ghcr.io/autamus/htop
Compressed Size : 29MB
```

## Description
htop is an interactive text-mode process viewer for Unix systems.

## Usage
### Pull (Download)
To download the latest version of htop run,

```bash
docker pull ghcr.io/autamus/htop:latest
```

or to download a specific version of htop run,

```bash
docker pull ghcr.io/autamus/htop:2.2.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/htop htop --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/htop bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the htop container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/htop htop /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC htop container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-htop/).
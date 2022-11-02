---
layout: container
name: rclone
github: https://github.com/autamus/registry/blob/main/containers/r/rclone/spack.yaml
versions:
- 1.51.0
- 1.55.0
- 1.55.1
- 1.56.0
- 1.56.1
- 1.56.2
- 1.57.0
- 1.59.1
updated_at: 2022-11-02T23:48:21.46227942Z
size: 48MB
description: Rclone is a command line program to sync files and directories to and
  from various cloud storage providers
container_url: https://github.com/orgs/autamus/packages/container/package/rclone

---
# rclone
```bash 
Download        : docker pull ghcr.io/autamus/rclone
Compressed Size : 48MB
```

## Description
Rclone is a command line program to sync files and directories to and from various cloud storage providers

## Usage
### Pull (Download)
To download the latest version of rclone run,

```bash
docker pull ghcr.io/autamus/rclone:latest
```

or to download a specific version of rclone run,

```bash
docker pull ghcr.io/autamus/rclone:1.51.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/rclone rclone --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/rclone bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the rclone container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/rclone rclone /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC rclone container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-rclone/).
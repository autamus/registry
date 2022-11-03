---
layout: container
name: wget
github: https://github.com/autamus/registry/blob/main/containers/w/wget/spack.yaml
versions:
- 1.21.1
- 1.21.3
updated_at: 2022-11-03T20:46:04.831546564Z
size: 33MB
description: GNU Wget is a free software package for retrieving files using HTTP,
  HTTPS and FTP, the most widely-used Internet protocols. It is a non-interactive
  commandline tool, so it may easily be called from scripts, cron jobs, terminals
  without X-Windows support, etc.
container_url: https://github.com/orgs/autamus/packages/container/package/wget

---
# wget
```bash 
Download        : docker pull ghcr.io/autamus/wget
Compressed Size : 33MB
```

## Description
GNU Wget is a free software package for retrieving files using HTTP, HTTPS and FTP, the most widely-used Internet protocols. It is a non-interactive commandline tool, so it may easily be called from scripts, cron jobs, terminals without X-Windows support, etc.

## Usage
### Pull (Download)
To download the latest version of wget run,

```bash
docker pull ghcr.io/autamus/wget:latest
```

or to download a specific version of wget run,

```bash
docker pull ghcr.io/autamus/wget:1.21.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/wget wget --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/wget bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the wget container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/wget wget /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC wget container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-wget/).
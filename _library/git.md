---
layout: container
name: git
github: https://github.com/autamus/registry/blob/main/containers/g/git/spack.yaml
versions:
- 2.35.2
- latest
updated_at: 2022-11-03T20:03:59.413482048Z
size: 316MB
description: 'Git is a free and open source distributed version control system designed
  to handle everything from small to very large projects with speed and efficiency. '
container_url: https://github.com/orgs/autamus/packages/container/package/git

---
# git
```bash 
Download        : docker pull ghcr.io/autamus/git
Compressed Size : 316MB
```

## Description
Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. 

## Usage
### Pull (Download)
To download the latest version of git run,

```bash
docker pull ghcr.io/autamus/git:latest
```

or to download a specific version of git run,

```bash
docker pull ghcr.io/autamus/git:2.35.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/git git --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/git bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the git container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/git git /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC git container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-git/).
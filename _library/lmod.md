---
layout: container
name: lmod
github: https://github.com/autamus/registry/blob/main/containers/l/lmod/spack.yaml
versions:
- "8.3"
- 8.5.12
- 8.5.13
- 8.5.27
- 8.5.6
- 8.5.7
- 8.5.8
- 8.5.9
- 8.6.3
updated_at: 2021-12-30T01:44:27.712946424Z
size: 45MB
description: ' homepage = ''https://www.tacc.utexas.edu/research-development/tacc-projects/lmod'
container_url: https://github.com/orgs/autamus/packages/container/package/lmod

---
# lmod
```bash 
Download        : docker pull ghcr.io/autamus/lmod
Compressed Size : 45MB
```

## Description
 homepage = 'https://www.tacc.utexas.edu/research-development/tacc-projects/lmod

## Usage
### Pull (Download)
To download the latest version of lmod run,

```bash
docker pull ghcr.io/autamus/lmod:latest
```

or to download a specific version of lmod run,

```bash
docker pull ghcr.io/autamus/lmod:8.3
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/lmod lmod --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/lmod bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the lmod container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/lmod lmod /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC lmod container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-lmod/).
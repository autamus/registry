---
layout: container
name: apr
github: https://github.com/autamus/registry/blob/main/containers/a/apr/spack.yaml
versions:
- 1.7.0
updated_at: 2022-08-01T17:50:48.326889781Z
size: 30MB
description: Apache portable runtime.
container_url: https://github.com/orgs/autamus/packages/container/package/apr

---
# apr
```bash 
Download        : docker pull ghcr.io/autamus/apr
Compressed Size : 30MB
```

## Description
Apache portable runtime.

## Usage
### Pull (Download)
To download the latest version of apr run,

```bash
docker pull ghcr.io/autamus/apr:latest
```

or to download a specific version of apr run,

```bash
docker pull ghcr.io/autamus/apr:1.7.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/apr apr --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/apr bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the apr container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/apr apr /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC apr container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-apr/).
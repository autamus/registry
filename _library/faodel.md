---
layout: container
name: faodel
github: https://github.com/autamus/registry/blob/main/containers/f/faodel/spack.yaml
versions:
- 1.1906.1
- 1.2108.1
updated_at: 2021-11-01T15:57:02.713979933Z
size: 75MB
description: Flexible, Asynchronous, Object Data-Exchange Libraries
container_url: https://github.com/orgs/autamus/packages/container/package/faodel

---
# faodel
```bash 
Download        : docker pull ghcr.io/autamus/faodel
Compressed Size : 75MB
```

## Description
Flexible, Asynchronous, Object Data-Exchange Libraries

## Usage
### Pull (Download)
To download the latest version of faodel run,

```bash
docker pull ghcr.io/autamus/faodel:latest
```

or to download a specific version of faodel run,

```bash
docker pull ghcr.io/autamus/faodel:1.1906.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/faodel faodel --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/faodel bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the faodel container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/faodel faodel /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC faodel container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-faodel/).
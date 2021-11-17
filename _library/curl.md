---
layout: container
name: curl
github: https://github.com/autamus/registry/blob/main/containers/c/curl/spack.yaml
versions:
- 7.76.1
- 7.78.0
- 7.79.0
- 7.80.0
updated_at: 2021-11-17T15:52:27.354063944Z
size: 31MB
description: cURL is an open source command line tool and library for transferring
  data with URL syntax
container_url: https://github.com/orgs/autamus/packages/container/package/curl

---
# curl
```bash 
Download        : docker pull ghcr.io/autamus/curl
Compressed Size : 31MB
```

## Description
cURL is an open source command line tool and library for transferring data with URL syntax

## Usage
### Pull (Download)
To download the latest version of curl run,

```bash
docker pull ghcr.io/autamus/curl:latest
```

or to download a specific version of curl run,

```bash
docker pull ghcr.io/autamus/curl:7.76.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/curl curl --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/curl bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the curl container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/curl curl /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC curl container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-curl/).
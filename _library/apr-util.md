---
layout: container
name: apr-util
github: https://github.com/autamus/registry/blob/main/containers/a/apr-util/spack.yaml
versions:
- 1.6.1
updated_at: 2022-01-09T16:12:50.611691305Z
size: 36MB
description: Apache Portable Runtime Utility
container_url: https://github.com/orgs/autamus/packages/container/package/apr-util

---
# apr-util
```bash 
Download        : docker pull ghcr.io/autamus/apr-util
Compressed Size : 36MB
```

## Description
Apache Portable Runtime Utility

## Usage
### Pull (Download)
To download the latest version of apr-util run,

```bash
docker pull ghcr.io/autamus/apr-util:latest
```

or to download a specific version of apr-util run,

```bash
docker pull ghcr.io/autamus/apr-util:1.6.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/apr-util apr-util --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/apr-util bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the apr-util container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/apr-util apr-util /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC apr-util container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-apr-util/).
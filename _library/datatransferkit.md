---
layout: container
name: datatransferkit
github: https://github.com/autamus/registry/blob/main/containers/d/datatransferkit/spack.yaml
versions:
- 3.1.rc.2
updated_at: 2021-06-23T19:28:15.328003229Z
size: 205MB
description: DataTransferKit is an open-source software library of parallel solution
  transfer services for multiphysics simulations
container_url: https://github.com/orgs/autamus/packages/container/package/datatransferkit

---
# datatransferkit
```bash 
Download        : docker pull ghcr.io/autamus/datatransferkit
Compressed Size : 205MB
```

## Description
DataTransferKit is an open-source software library of parallel solution transfer services for multiphysics simulations

## Usage
### Pull (Download)
To download the latest version of datatransferkit run,

```bash
docker pull ghcr.io/autamus/datatransferkit:latest
```

or to download a specific version of datatransferkit run,

```bash
docker pull ghcr.io/autamus/datatransferkit:3.1.rc.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/datatransferkit datatransferkit --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/datatransferkit bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the datatransferkit container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/datatransferkit datatransferkit /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC datatransferkit container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-datatransferkit/).
---
layout: container
name: libnrm
github: https://github.com/autamus/registry/blob/main/containers/l/libnrm/spack.yaml
versions:
- 0.1.0
updated_at: 2022-01-11T15:21:46.783054263Z
size: 51MB
description: Libnrm, the application instrumentation library for the Node Resource
  Manager(NRM).
container_url: https://github.com/orgs/autamus/packages/container/package/libnrm

---
# libnrm
```bash 
Download        : docker pull ghcr.io/autamus/libnrm
Compressed Size : 51MB
```

## Description
Libnrm, the application instrumentation library for the Node Resource Manager(NRM).

## Usage
### Pull (Download)
To download the latest version of libnrm run,

```bash
docker pull ghcr.io/autamus/libnrm:latest
```

or to download a specific version of libnrm run,

```bash
docker pull ghcr.io/autamus/libnrm:0.1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/libnrm libnrm --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/libnrm bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the libnrm container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/libnrm libnrm /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC libnrm container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-libnrm/).
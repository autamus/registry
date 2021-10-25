---
layout: container
name: veloc
github: https://github.com/autamus/registry/blob/main/containers/v/veloc/spack.yaml
versions:
- "1.4"
- "1.5"
updated_at: 2021-10-25T16:51:08.846723407Z
size: 74MB
description: Very-Low Overhead Checkpointing System. VELOC is a multi-level checkpoint-restart
  runtime for HPC supercomputing infrastructures
container_url: https://github.com/orgs/autamus/packages/container/package/veloc

---
# veloc
```bash 
Download        : docker pull ghcr.io/autamus/veloc
Compressed Size : 74MB
```

## Description
Very-Low Overhead Checkpointing System. VELOC is a multi-level checkpoint-restart runtime for HPC supercomputing infrastructures

## Usage
### Pull (Download)
To download the latest version of veloc run,

```bash
docker pull ghcr.io/autamus/veloc:latest
```

or to download a specific version of veloc run,

```bash
docker pull ghcr.io/autamus/veloc:1.4
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/veloc veloc --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/veloc bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the veloc container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/veloc veloc /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC veloc container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-veloc/).
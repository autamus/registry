---
layout: container
name: accumulo
github: https://github.com/autamus/registry/blob/main/containers/a/accumulo/spack.yaml
versions:
- 2.0.0
- 2.0.1
updated_at: 2022-08-01T17:53:13.637705817Z
size: 274MB
description: Apache Accumulo is a sorted, distributed key/value store that provides
  robust, scalable data storage and retrieval.
container_url: https://github.com/orgs/autamus/packages/container/package/accumulo

---
# accumulo
```bash 
Download        : docker pull ghcr.io/autamus/accumulo
Compressed Size : 274MB
```

## Description
Apache Accumulo is a sorted, distributed key/value store that provides robust, scalable data storage and retrieval.

## Usage
### Pull (Download)
To download the latest version of accumulo run,

```bash
docker pull ghcr.io/autamus/accumulo:latest
```

or to download a specific version of accumulo run,

```bash
docker pull ghcr.io/autamus/accumulo:2.0.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/accumulo accumulo --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/accumulo bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the accumulo container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/accumulo accumulo /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC accumulo container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-accumulo/).
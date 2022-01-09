---
layout: container
name: protobuf
github: https://github.com/autamus/registry/blob/main/containers/p/protobuf/spack.yaml
versions:
- 3.17.3
- 3.18.0
- 3.18.1
- 3.19.0
- 3.19.1
updated_at: 2022-01-09T16:31:54.96201349Z
size: 30MB
description: Google's data interchange format.
container_url: https://github.com/orgs/autamus/packages/container/package/protobuf

---
# protobuf
```bash 
Download        : docker pull ghcr.io/autamus/protobuf
Compressed Size : 30MB
```

## Description
Google's data interchange format.

## Usage
### Pull (Download)
To download the latest version of protobuf run,

```bash
docker pull ghcr.io/autamus/protobuf:latest
```

or to download a specific version of protobuf run,

```bash
docker pull ghcr.io/autamus/protobuf:3.17.3
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/protobuf protobuf --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/protobuf bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the protobuf container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/protobuf protobuf /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC protobuf container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-protobuf/).
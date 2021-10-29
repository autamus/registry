---
layout: container
name: go
github: https://github.com/autamus/registry/blob/main/containers/g/go/spack.yaml
versions:
- 1.16.0
- 1.16.2
- 1.16.3
- 1.16.4
- 1.16.5
- 1.16.6
- 1.16.7
- "1.17"
- 1.17.1
- 1.17.2
updated_at: 2021-10-29T15:04:25.697892894Z
size: 296MB
description: The golang compiler and build environment
container_url: https://github.com/orgs/autamus/packages/container/package/go

---
# go
```bash 
Download        : docker pull ghcr.io/autamus/go
Compressed Size : 296MB
```

## Description
The golang compiler and build environment

## Usage
### Pull (Download)
To download the latest version of go run,

```bash
docker pull ghcr.io/autamus/go:latest
```

or to download a specific version of go run,

```bash
docker pull ghcr.io/autamus/go:1.16.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/go go --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/go bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the go container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/go go /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC go container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-go/).
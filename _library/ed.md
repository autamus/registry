---
layout: container
name: ed
github: https://github.com/autamus/registry/blob/main/containers/e/ed/spack.yaml
versions:
- "1.4"
updated_at: 2022-01-15T15:49:49.671634338Z
size: 26MB
description: GNU ed is a line-oriented text editor. It is used to create, display,
  modify and otherwise manipulate text files, both interactively and via shell scripts.
container_url: https://github.com/orgs/autamus/packages/container/package/ed

---
# ed
```bash 
Download        : docker pull ghcr.io/autamus/ed
Compressed Size : 26MB
```

## Description
GNU ed is a line-oriented text editor. It is used to create, display, modify and otherwise manipulate text files, both interactively and via shell scripts.

## Usage
### Pull (Download)
To download the latest version of ed run,

```bash
docker pull ghcr.io/autamus/ed:latest
```

or to download a specific version of ed run,

```bash
docker pull ghcr.io/autamus/ed:1.4
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/ed ed --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/ed bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the ed container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/ed ed /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC ed container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-ed/).
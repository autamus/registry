---
layout: container
name: cowsay
github: https://github.com/autamus/registry/blob/main/containers/c/cowsay/spack.yaml
versions:
- "3.04"
updated_at: 2022-10-27T17:22:25.724429519Z
size: 47MB
description: A program that generates ASCII pictures of a cow with a message.
container_url: https://github.com/orgs/autamus/packages/container/package/cowsay

---
# cowsay
```bash 
Download        : docker pull ghcr.io/autamus/cowsay
Compressed Size : 47MB
```

## Description
A program that generates ASCII pictures of a cow with a message.

## Usage
### Pull (Download)
To download the latest version of cowsay run,

```bash
docker pull ghcr.io/autamus/cowsay:latest
```

or to download a specific version of cowsay run,

```bash
docker pull ghcr.io/autamus/cowsay:3.04
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/cowsay cowsay --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/cowsay bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the cowsay container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/cowsay cowsay /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC cowsay container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-cowsay/).
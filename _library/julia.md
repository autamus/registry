---
layout: container
name: julia
github: https://github.com/autamus/registry/blob/main/containers/j/julia/spack.yaml
versions:
- 1.5.3
- 1.5.4
- 1.6.0
- 1.6.1
- 1.6.2
- 1.6.3
updated_at: 2021-10-25T17:02:56.922015041Z
size: 104MB
description: 'The Julia Language: A fresh approach to technical computing'
container_url: https://github.com/orgs/autamus/packages/container/package/julia

---
# julia
```bash 
Download        : docker pull ghcr.io/autamus/julia
Compressed Size : 104MB
```

## Description
The Julia Language: A fresh approach to technical computing

## Usage
### Pull (Download)
To download the latest version of julia run,

```bash
docker pull ghcr.io/autamus/julia:latest
```

or to download a specific version of julia run,

```bash
docker pull ghcr.io/autamus/julia:1.5.3
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/julia julia --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/julia bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the julia container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/julia julia /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC julia container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-julia/).
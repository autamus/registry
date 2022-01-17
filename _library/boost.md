---
layout: container
name: boost
github: https://github.com/autamus/registry/blob/main/containers/b/boost/spack.yaml
versions:
- 1.75.0
- 1.76.0
- 1.77.0
- 1.78.0
updated_at: 2022-01-17T16:32:05.830995139Z
size: 48MB
description: 'Boost provides free peer-reviewed portable C++ source libraries, emphasizing
  libraries that work well with the C++ Standard Library. Boost libraries are intended
  to be widely useful, and usable across a broad spectrum of applications. The Boost
  license encourages both commercial and non-commercial use. '
container_url: https://github.com/orgs/autamus/packages/container/package/boost

---
# boost
```bash 
Download        : docker pull ghcr.io/autamus/boost
Compressed Size : 48MB
```

## Description
Boost provides free peer-reviewed portable C++ source libraries, emphasizing libraries that work well with the C++ Standard Library. Boost libraries are intended to be widely useful, and usable across a broad spectrum of applications. The Boost license encourages both commercial and non-commercial use. 

## Usage
### Pull (Download)
To download the latest version of boost run,

```bash
docker pull ghcr.io/autamus/boost:latest
```

or to download a specific version of boost run,

```bash
docker pull ghcr.io/autamus/boost:1.75.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/boost boost --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/boost bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the boost container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/boost boost /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC boost container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-boost/).
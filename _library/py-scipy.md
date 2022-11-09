---
layout: container
name: py-scipy
github: https://github.com/autamus/registry/blob/main/containers/p/py-scipy/spack.yaml
versions:
- 1.6.3
- 1.7.0
- 1.7.1
- 1.7.2
- 1.7.3
- 1.8.1
updated_at: 2022-11-09T23:35:53.498021043Z
size: 153MB
description: SciPy (pronounced "Sigh
container_url: https://github.com/orgs/autamus/packages/container/package/py-scipy

---
# py-scipy
```bash 
Download        : docker pull ghcr.io/autamus/py-scipy
Compressed Size : 153MB
```

## Description
SciPy (pronounced "Sigh

## Usage
### Pull (Download)
To download the latest version of py-scipy run,

```bash
docker pull ghcr.io/autamus/py-scipy:latest
```

or to download a specific version of py-scipy run,

```bash
docker pull ghcr.io/autamus/py-scipy:1.6.3
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/py-scipy py-scipy --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/py-scipy bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the py-scipy container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/py-scipy py-scipy /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC py-scipy container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-py-scipy/).
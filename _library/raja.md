---
layout: container
name: raja
github: https://github.com/autamus/registry/blob/main/containers/r/raja/spack.yaml
versions:
- 0.13.0
- 0.14.0
updated_at: 2021-10-19T07:50:38.261013251Z
size: 65MB
description: RAJA Parallel Framework.
container_url: https://github.com/orgs/autamus/packages/container/package/raja

---
# raja
```bash 
Download        : docker pull ghcr.io/autamus/raja
Compressed Size : 65MB
```

## Description
RAJA Parallel Framework.

## Usage
### Pull (Download)
To download the latest version of raja run,

```bash
docker pull ghcr.io/autamus/raja:latest
```

or to download a specific version of raja run,

```bash
docker pull ghcr.io/autamus/raja:0.13.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/raja raja --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/raja bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the raja container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/raja raja /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC raja container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-raja/).
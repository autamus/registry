---
layout: container
name: cctools
github: https://github.com/autamus/registry/blob/main/containers/c/cctools/spack.yaml
versions:
- 7.2.10
updated_at: 2021-11-17T15:49:16.335101509Z
size: 113MB
description: 'The Cooperative Computing Tools (cctools) enable large scale distributed
  computations to harness hundreds to thousands of machines from clusters, clouds,
  and grids. '
container_url: https://github.com/orgs/autamus/packages/container/package/cctools

---
# cctools
```bash 
Download        : docker pull ghcr.io/autamus/cctools
Compressed Size : 113MB
```

## Description
The Cooperative Computing Tools (cctools) enable large scale distributed computations to harness hundreds to thousands of machines from clusters, clouds, and grids. 

## Usage
### Pull (Download)
To download the latest version of cctools run,

```bash
docker pull ghcr.io/autamus/cctools:latest
```

or to download a specific version of cctools run,

```bash
docker pull ghcr.io/autamus/cctools:7.2.10
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/cctools cctools --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/cctools bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the cctools container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/cctools cctools /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC cctools container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-cctools/).
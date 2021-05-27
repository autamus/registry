---
layout: container
name: singularity
github: https://github.com/autamus/registry/blob/main/containers/s/singularity/spack.yaml
versions:
- 3.7.4
updated_at: 2021-05-27T17:29:39.191273394Z
size: 343MB
description: ""
container_url: https://github.com/orgs/autamus/packages/container/package/singularity

---
# singularity
```bash 
Download        : docker pull ghcr.io/autamus/singularity
Compressed Size : 343MB
```

## Description


## Usage
### Pull (Download)
To download the latest version of singularity run,

```bash
docker pull ghcr.io/autamus/singularity:latest
```

or to download a specific version of singularity run,

```bash
docker pull ghcr.io/autamus/singularity:3.7.4
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/singularity singularity --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/singularity bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the singularity container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/singularity singularity /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC singularity container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-singularity/).
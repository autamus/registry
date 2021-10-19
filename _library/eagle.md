---
layout: container
name: eagle
github: https://github.com/autamus/registry/blob/main/containers/e/eagle/spack.yaml
versions:
- 1.1.2
updated_at: 2021-10-19T07:23:53.740000263Z
size: 35MB
description: 'EAGLE: Explicit Alternative Genome Likelihood Evaluator'
container_url: https://github.com/orgs/autamus/packages/container/package/eagle

---
# eagle
```bash 
Download        : docker pull ghcr.io/autamus/eagle
Compressed Size : 35MB
```

## Description
EAGLE: Explicit Alternative Genome Likelihood Evaluator

## Usage
### Pull (Download)
To download the latest version of eagle run,

```bash
docker pull ghcr.io/autamus/eagle:latest
```

or to download a specific version of eagle run,

```bash
docker pull ghcr.io/autamus/eagle:1.1.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/eagle eagle --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/eagle bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the eagle container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/eagle eagle /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC eagle container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-eagle/).
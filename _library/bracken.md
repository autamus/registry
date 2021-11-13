---
layout: container
name: bracken
github: https://github.com/autamus/registry/blob/main/containers/b/bracken/spack.yaml
versions:
- 1.0.0
updated_at: 2021-11-13T18:46:05.220217257Z
size: 102MB
description: Bracken (Bayesian Reestimation of Abundance with KrakEN) is a highly
  accurate statistical method that computes the abundance of species in DNA sequences
  from a metagenomics sample.
container_url: https://github.com/orgs/autamus/packages/container/package/bracken

---
# bracken
```bash 
Download        : docker pull ghcr.io/autamus/bracken
Compressed Size : 102MB
```

## Description
Bracken (Bayesian Reestimation of Abundance with KrakEN) is a highly accurate statistical method that computes the abundance of species in DNA sequences from a metagenomics sample.

## Usage
### Pull (Download)
To download the latest version of bracken run,

```bash
docker pull ghcr.io/autamus/bracken:latest
```

or to download a specific version of bracken run,

```bash
docker pull ghcr.io/autamus/bracken:1.0.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/bracken bracken --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/bracken bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the bracken container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/bracken bracken /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC bracken container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-bracken/).
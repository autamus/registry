---
layout: container
name: viennarna
github: https://github.com/autamus/registry/blob/main/containers/v/viennarna/spack.yaml
versions:
- 2.4.3
updated_at: 2021-11-01T16:19:54.886882868Z
size: 128MB
description: 'The ViennaRNA Package consists of a C code library and several stand-alone
  programs for the prediction and comparison of RNA secondary structures. '
container_url: https://github.com/orgs/autamus/packages/container/package/viennarna

---
# viennarna
```bash 
Download        : docker pull ghcr.io/autamus/viennarna
Compressed Size : 128MB
```

## Description
The ViennaRNA Package consists of a C code library and several stand-alone programs for the prediction and comparison of RNA secondary structures. 

## Usage
### Pull (Download)
To download the latest version of viennarna run,

```bash
docker pull ghcr.io/autamus/viennarna:latest
```

or to download a specific version of viennarna run,

```bash
docker pull ghcr.io/autamus/viennarna:2.4.3
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/viennarna viennarna --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/viennarna bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the viennarna container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/viennarna viennarna /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC viennarna container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-viennarna/).
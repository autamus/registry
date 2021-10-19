---
layout: container
name: clingo-bootstrap
github: https://github.com/autamus/registry/blob/main/containers/c/clingo-bootstrap/spack.yaml
versions:
- latest
updated_at: 2021-10-19T07:23:29.37614408Z
size: 87MB
description: Clingo with some options used for bootstrapping
container_url: https://github.com/orgs/autamus/packages/container/package/clingo-bootstrap

---
# clingo-bootstrap
```bash 
Download        : docker pull ghcr.io/autamus/clingo-bootstrap
Compressed Size : 87MB
```

## Description
Clingo with some options used for bootstrapping

## Usage
### Pull (Download)
To download the latest version of clingo-bootstrap run,

```bash
docker pull ghcr.io/autamus/clingo-bootstrap:latest
```

or to download a specific version of clingo-bootstrap run,

```bash
docker pull ghcr.io/autamus/clingo-bootstrap:latest
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/clingo-bootstrap clingo-bootstrap --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/clingo-bootstrap bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the clingo-bootstrap container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/clingo-bootstrap clingo-bootstrap /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC clingo-bootstrap container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-clingo-bootstrap/).
---
layout: container
name: openbabel
github: https://github.com/autamus/registry/blob/main/containers/o/openbabel/spack.yaml
versions:
- 3.0.0
- 3.1.1
updated_at: 2021-11-12T16:11:52.161538669Z
size: 197MB
description: Open Babel is a chemical toolbox designed to speak the many languages
  of chemical data. It's an open, collaborative project allowing anyone to search,
  convert, analyze, or store data from molecular modeling, chemistry, solid-state
  materials, biochemistry, or related areas.
container_url: https://github.com/orgs/autamus/packages/container/package/openbabel

---
# openbabel
```bash 
Download        : docker pull ghcr.io/autamus/openbabel
Compressed Size : 197MB
```

## Description
Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It's an open, collaborative project allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, biochemistry, or related areas.

## Usage
### Pull (Download)
To download the latest version of openbabel run,

```bash
docker pull ghcr.io/autamus/openbabel:latest
```

or to download a specific version of openbabel run,

```bash
docker pull ghcr.io/autamus/openbabel:3.0.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/openbabel openbabel --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/openbabel bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the openbabel container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/openbabel openbabel /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC openbabel container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-openbabel/).
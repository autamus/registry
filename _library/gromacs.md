---
layout: container
name: gromacs
github: https://github.com/autamus/registry/blob/main/containers/g/gromacs/spack.yaml
versions:
- "2021.1"
- "2021.2"
- "2021.3"
- "2021.4"
- "2022.3"
updated_at: 2022-11-06T20:58:20.539742746Z
size: 80MB
description: 'GROMACS (GROningen MAchine for Chemical Simulations) is a molecular
  dynamics package primarily designed for simulations of proteins, lipids and nucleic
  acids. It was originally developed in the Biophysical Chemistry department of University
  of Groningen, and is now maintained by contributors in universities and research
  centers across the world. GROMACS is one of the fastest and most popular software
  packages available and can run on CPUs as well as GPUs. It is free, open source
  released under the GNU General Public License. Starting from version 4.6, GROMACS
  is released under the GNU Lesser General Public License. '
container_url: https://github.com/orgs/autamus/packages/container/package/gromacs

---
# gromacs
```bash 
Download        : docker pull ghcr.io/autamus/gromacs
Compressed Size : 80MB
```

## Description
GROMACS (GROningen MAchine for Chemical Simulations) is a molecular dynamics package primarily designed for simulations of proteins, lipids and nucleic acids. It was originally developed in the Biophysical Chemistry department of University of Groningen, and is now maintained by contributors in universities and research centers across the world. GROMACS is one of the fastest and most popular software packages available and can run on CPUs as well as GPUs. It is free, open source released under the GNU General Public License. Starting from version 4.6, GROMACS is released under the GNU Lesser General Public License. 

## Usage
### Pull (Download)
To download the latest version of gromacs run,

```bash
docker pull ghcr.io/autamus/gromacs:latest
```

or to download a specific version of gromacs run,

```bash
docker pull ghcr.io/autamus/gromacs:2021.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/gromacs gromacs --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/gromacs bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the gromacs container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/gromacs gromacs /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC gromacs container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-gromacs/).
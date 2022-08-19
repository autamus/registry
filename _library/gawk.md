---
layout: container
name: gawk
github: https://github.com/autamus/registry/blob/main/containers/g/gawk/spack.yaml
versions:
- 5.1.0
- 5.1.1
updated_at: 2022-08-19T16:53:28.68947721Z
size: 34MB
description: 'If you are like many computer users, you would frequently like to make
  changes in various text files wherever certain patterns appear, or extract data
  from parts of certain lines while discarding the rest. To write a program to do
  this in a language such as C or Pascal is a time-consuming inconvenience that may
  take many lines of code. The job is easy with awk, especially the GNU implementation:
  gawk. The awk utility interprets a special-purpose programming language that makes
  it possible to handle simple data-reformatting jobs with just a few lines of code. '
container_url: https://github.com/orgs/autamus/packages/container/package/gawk

---
# gawk
```bash 
Download        : docker pull ghcr.io/autamus/gawk
Compressed Size : 34MB
```

## Description
If you are like many computer users, you would frequently like to make changes in various text files wherever certain patterns appear, or extract data from parts of certain lines while discarding the rest. To write a program to do this in a language such as C or Pascal is a time-consuming inconvenience that may take many lines of code. The job is easy with awk, especially the GNU implementation: gawk. The awk utility interprets a special-purpose programming language that makes it possible to handle simple data-reformatting jobs with just a few lines of code. 

## Usage
### Pull (Download)
To download the latest version of gawk run,

```bash
docker pull ghcr.io/autamus/gawk:latest
```

or to download a specific version of gawk run,

```bash
docker pull ghcr.io/autamus/gawk:5.1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/gawk gawk --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/gawk bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the gawk container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/gawk gawk /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC gawk container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-gawk/).
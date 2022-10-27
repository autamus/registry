---
layout: container
name: perl
github: https://github.com/autamus/registry/blob/main/containers/p/perl/spack.yaml
versions:
- 5.35.0
updated_at: 2022-10-27T18:09:51.944707661Z
size: 47MB
description: Perl 5 is a highly capable, feature-rich programming language with over
  27 years of development.
container_url: https://github.com/orgs/autamus/packages/container/package/perl

---
# perl
```bash 
Download        : docker pull ghcr.io/autamus/perl
Compressed Size : 47MB
```

## Description
Perl 5 is a highly capable, feature-rich programming language with over 27 years of development.

## Usage
### Pull (Download)
To download the latest version of perl run,

```bash
docker pull ghcr.io/autamus/perl:latest
```

or to download a specific version of perl run,

```bash
docker pull ghcr.io/autamus/perl:5.35.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/perl perl --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/perl bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the perl container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/perl perl /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC perl container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-perl/).
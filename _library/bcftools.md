---
layout: container
name: bcftools
github: https://github.com/autamus/registry/blob/main/containers/b/bcftools/spack.yaml
versions:
- "1.11"
- "1.12"
- "1.13"
- "1.14"
updated_at: 2021-12-30T16:01:30.811148278Z
size: 159MB
description: BCFtools is a set of utilities that manipulate variant calls in the Variant
  Call Format (VCF) and its binary counterpart BCF. All commands work transparently
  with both VCFs and BCFs, both uncompressed and BGZF-compressed.
container_url: https://github.com/orgs/autamus/packages/container/package/bcftools

---
# bcftools
```bash 
Download        : docker pull ghcr.io/autamus/bcftools
Compressed Size : 159MB
```

## Description
BCFtools is a set of utilities that manipulate variant calls in the Variant Call Format (VCF) and its binary counterpart BCF. All commands work transparently with both VCFs and BCFs, both uncompressed and BGZF-compressed.

## Usage
### Pull (Download)
To download the latest version of bcftools run,

```bash
docker pull ghcr.io/autamus/bcftools:latest
```

or to download a specific version of bcftools run,

```bash
docker pull ghcr.io/autamus/bcftools:1.11
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/bcftools bcftools --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/bcftools bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the bcftools container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/bcftools bcftools /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC bcftools container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-bcftools/).
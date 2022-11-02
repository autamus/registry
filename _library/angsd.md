---
layout: container
name: angsd
github: https://github.com/autamus/registry/blob/main/containers/a/angsd/spack.yaml
versions:
- "0.933"
- "0.935"
updated_at: 2022-11-02T21:22:50.556892632Z
size: 289MB
description: Angsd is a program for analysing NGS data. The software can handle a
  number of different input types from mapped reads to imputed genotype probabilities.
  Most methods take genotype uncertainty into account instead of basing the analysis
  on called genotypes. This is especially useful for low and medium depth data.
container_url: https://github.com/orgs/autamus/packages/container/package/angsd

---
# angsd
```bash 
Download        : docker pull ghcr.io/autamus/angsd
Compressed Size : 289MB
```

## Description
Angsd is a program for analysing NGS data. The software can handle a number of different input types from mapped reads to imputed genotype probabilities. Most methods take genotype uncertainty into account instead of basing the analysis on called genotypes. This is especially useful for low and medium depth data.

## Usage
### Pull (Download)
To download the latest version of angsd run,

```bash
docker pull ghcr.io/autamus/angsd:latest
```

or to download a specific version of angsd run,

```bash
docker pull ghcr.io/autamus/angsd:0.933
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/angsd angsd --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/angsd bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the angsd container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/angsd angsd /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC angsd container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-angsd/).
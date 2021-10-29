---
layout: container
name: admixtools
github: https://github.com/autamus/registry/blob/main/containers/a/admixtools/spack.yaml
versions:
- 7.0.1
- 7.0.2
updated_at: 2021-10-29T14:57:04.591005552Z
size: 58MB
description: The ADMIXTOOLS package implements 5 methods described in Patterson et
  al. (2012) Ancient Admixture in Human History. Details of the methods and algorithm
  can be found in this paper..
container_url: https://github.com/orgs/autamus/packages/container/package/admixtools

---
# admixtools
```bash 
Download        : docker pull ghcr.io/autamus/admixtools
Compressed Size : 58MB
```

## Description
The ADMIXTOOLS package implements 5 methods described in Patterson et al. (2012) Ancient Admixture in Human History. Details of the methods and algorithm can be found in this paper..

## Usage
### Pull (Download)
To download the latest version of admixtools run,

```bash
docker pull ghcr.io/autamus/admixtools:latest
```

or to download a specific version of admixtools run,

```bash
docker pull ghcr.io/autamus/admixtools:7.0.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/admixtools admixtools --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/admixtools bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the admixtools container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/admixtools admixtools /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC admixtools container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-admixtools/).
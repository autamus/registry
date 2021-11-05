---
layout: container
name: kallisto
github: https://github.com/autamus/registry/blob/main/containers/k/kallisto/spack.yaml
versions:
- 0.46.2
updated_at: 2021-11-05T15:07:21.461342686Z
size: 86MB
description: kallisto is a program for quantifying abundances of transcripts from
  RNA-Seq data.
container_url: https://github.com/orgs/autamus/packages/container/package/kallisto

---
# kallisto
```bash 
Download        : docker pull ghcr.io/autamus/kallisto
Compressed Size : 86MB
```

## Description
kallisto is a program for quantifying abundances of transcripts from RNA-Seq data.

## Usage
### Pull (Download)
To download the latest version of kallisto run,

```bash
docker pull ghcr.io/autamus/kallisto:latest
```

or to download a specific version of kallisto run,

```bash
docker pull ghcr.io/autamus/kallisto:0.46.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/kallisto kallisto --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/kallisto bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the kallisto container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/kallisto kallisto /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC kallisto container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-kallisto/).
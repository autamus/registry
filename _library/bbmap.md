---
layout: container
name: bbmap
github: https://github.com/autamus/registry/blob/main/containers/b/bbmap/spack.yaml
versions:
- "38.63"
updated_at: 2022-01-15T15:44:56.276487848Z
size: 231MB
description: Short read aligner for DNA and RNA-seq data.
container_url: https://github.com/orgs/autamus/packages/container/package/bbmap

---
# bbmap
```bash 
Download        : docker pull ghcr.io/autamus/bbmap
Compressed Size : 231MB
```

## Description
Short read aligner for DNA and RNA-seq data.

## Usage
### Pull (Download)
To download the latest version of bbmap run,

```bash
docker pull ghcr.io/autamus/bbmap:latest
```

or to download a specific version of bbmap run,

```bash
docker pull ghcr.io/autamus/bbmap:38.63
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/bbmap bbmap --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/bbmap bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the bbmap container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/bbmap bbmap /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC bbmap container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-bbmap/).
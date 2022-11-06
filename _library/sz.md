---
layout: container
name: sz
github: https://github.com/autamus/registry/blob/main/containers/s/sz/spack.yaml
versions:
- 2.1.11.1
- 2.1.11.2
- 2.1.12
- 2.1.12.2
updated_at: 2022-11-06T20:56:33.432609964Z
size: 28MB
description: Error-bounded Lossy Compressor for HPC Data
container_url: https://github.com/orgs/autamus/packages/container/package/sz

---
# sz
```bash 
Download        : docker pull ghcr.io/autamus/sz
Compressed Size : 28MB
```

## Description
Error-bounded Lossy Compressor for HPC Data

## Usage
### Pull (Download)
To download the latest version of sz run,

```bash
docker pull ghcr.io/autamus/sz:latest
```

or to download a specific version of sz run,

```bash
docker pull ghcr.io/autamus/sz:2.1.11.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/sz sz --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/sz bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the sz container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/sz sz /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC sz container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-sz/).
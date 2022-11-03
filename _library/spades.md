---
layout: container
name: spades
github: https://github.com/autamus/registry/blob/main/containers/s/spades/spack.yaml
versions:
- 3.15.0
- 3.15.2
- 3.15.3
updated_at: 2022-11-03T00:13:22.102536517Z
size: 107MB
description: SPAdes - St. Petersburg genome assembler - is intended for both standard
  isolates and single-cell MDA bacteria assemblies.
container_url: https://github.com/orgs/autamus/packages/container/package/spades

---
# spades
```bash 
Download        : docker pull ghcr.io/autamus/spades
Compressed Size : 107MB
```

## Description
SPAdes - St. Petersburg genome assembler - is intended for both standard isolates and single-cell MDA bacteria assemblies.

## Usage
### Pull (Download)
To download the latest version of spades run,

```bash
docker pull ghcr.io/autamus/spades:latest
```

or to download a specific version of spades run,

```bash
docker pull ghcr.io/autamus/spades:3.15.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/spades spades --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/spades bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the spades container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/spades spades /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC spades container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-spades/).
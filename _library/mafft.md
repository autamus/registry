---
layout: container
name: mafft
github: https://github.com/autamus/registry/blob/main/containers/m/mafft/spack.yaml
versions:
- "7.481"
updated_at: 2022-08-01T19:03:36.032544015Z
size: 34MB
description: MAFFT is a multiple sequence alignment program for unix-like operating
  systems. It offers a range of multiple alignment methods, L-INS-i (accurate; for
  alignment of <~200 sequences), FFT-NS-2 (fast; for alignment of <~30,000 sequences),
  etc.
container_url: https://github.com/orgs/autamus/packages/container/package/mafft

---
# mafft
```bash 
Download        : docker pull ghcr.io/autamus/mafft
Compressed Size : 34MB
```

## Description
MAFFT is a multiple sequence alignment program for unix-like operating systems. It offers a range of multiple alignment methods, L-INS-i (accurate; for alignment of <~200 sequences), FFT-NS-2 (fast; for alignment of <~30,000 sequences), etc.

## Usage
### Pull (Download)
To download the latest version of mafft run,

```bash
docker pull ghcr.io/autamus/mafft:latest
```

or to download a specific version of mafft run,

```bash
docker pull ghcr.io/autamus/mafft:7.481
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/mafft mafft --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/mafft bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the mafft container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/mafft mafft /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC mafft container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-mafft/).
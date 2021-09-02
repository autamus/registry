---
layout: container
name: bart
github: https://github.com/autamus/registry/blob/main/containers/b/bart/spack.yaml
versions:
- 0.7.00
updated_at: 2021-09-02T01:58:48.558064357Z
size: 154MB
description: 'BART: Toolbox for Computational Magnetic Resonance Imaging'
container_url: https://github.com/orgs/autamus/packages/container/package/bart

---
# bart
```bash 
Download        : docker pull ghcr.io/autamus/bart
Compressed Size : 154MB
```

## Description
BART: Toolbox for Computational Magnetic Resonance Imaging

## Usage
### Pull (Download)
To download the latest version of bart run,

```bash
docker pull ghcr.io/autamus/bart:latest
```

or to download a specific version of bart run,

```bash
docker pull ghcr.io/autamus/bart:0.7.00
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/bart bart --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/bart bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the bart container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/bart bart /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC bart container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-bart/).
---
layout: container
name: snappy
github: https://github.com/autamus/registry/blob/main/containers/s/snappy/spack.yaml
versions:
- 1.1.8
updated_at: 2021-08-25T06:16:43.110103568Z
size: 26MB
description: 'A fast compressor/decompressor: https://code.google.com/p/snappy'
container_url: https://github.com/orgs/autamus/packages/container/package/snappy

---
# snappy
```bash 
Download        : docker pull ghcr.io/autamus/snappy
Compressed Size : 26MB
```

## Description
A fast compressor/decompressor: https://code.google.com/p/snappy

## Usage
### Pull (Download)
To download the latest version of snappy run,

```bash
docker pull ghcr.io/autamus/snappy:latest
```

or to download a specific version of snappy run,

```bash
docker pull ghcr.io/autamus/snappy:1.1.8
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/snappy snappy --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/snappy bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the snappy container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/snappy snappy /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC snappy container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-snappy/).
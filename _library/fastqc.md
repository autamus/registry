---
layout: container
name: fastqc
github: https://github.com/autamus/registry/blob/main/containers/f/fastqc/spack.yaml
versions:
- 0.11.9
updated_at: 2021-10-19T07:25:26.908533475Z
size: 249MB
description: A quality control tool for high throughput sequence data.
container_url: https://github.com/orgs/autamus/packages/container/package/fastqc

---
# fastqc
```bash 
Download        : docker pull ghcr.io/autamus/fastqc
Compressed Size : 249MB
```

## Description
A quality control tool for high throughput sequence data.

## Usage
### Pull (Download)
To download the latest version of fastqc run,

```bash
docker pull ghcr.io/autamus/fastqc:latest
```

or to download a specific version of fastqc run,

```bash
docker pull ghcr.io/autamus/fastqc:0.11.9
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/fastqc fastqc --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/fastqc bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the fastqc container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/fastqc fastqc /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC fastqc container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-fastqc/).
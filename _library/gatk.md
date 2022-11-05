---
layout: container
name: gatk
github: https://github.com/autamus/registry/blob/main/containers/g/gatk/spack.yaml
versions:
- 4.2.0.0
- 4.2.2.0
- 4.2.3.0
- 4.2.6.1
updated_at: 2022-11-05T20:43:03.056793643Z
size: 728MB
description: ' Genome Analysis Toolkit Variant Discovery in High-Throughput Sequencing
  Data '
container_url: https://github.com/orgs/autamus/packages/container/package/gatk

---
# gatk
```bash 
Download        : docker pull ghcr.io/autamus/gatk
Compressed Size : 728MB
```

## Description
 Genome Analysis Toolkit Variant Discovery in High-Throughput Sequencing Data 

## Usage
### Pull (Download)
To download the latest version of gatk run,

```bash
docker pull ghcr.io/autamus/gatk:latest
```

or to download a specific version of gatk run,

```bash
docker pull ghcr.io/autamus/gatk:4.2.0.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/gatk gatk --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/gatk bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the gatk container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/gatk gatk /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC gatk container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-gatk/).
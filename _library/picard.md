---
layout: container
name: picard
github: https://github.com/autamus/registry/blob/main/containers/p/picard/spack.yaml
versions:
- 2.24.0
- 2.25.0
- 2.25.1
- 2.25.2
- 2.25.3
- 2.25.4
- 2.25.5
- 2.25.6
- 2.25.7
- 2.26.0
- 2.26.2
- 2.26.3
- 2.26.4
updated_at: 2021-10-29T18:22:08.315983189Z
size: 235MB
description: 'Picard is a set of command line tools for manipulating high-throughput
  sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF. '
container_url: https://github.com/orgs/autamus/packages/container/package/picard

---
# picard
```bash 
Download        : docker pull ghcr.io/autamus/picard
Compressed Size : 235MB
```

## Description
Picard is a set of command line tools for manipulating high-throughput sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF. 

## Usage
### Pull (Download)
To download the latest version of picard run,

```bash
docker pull ghcr.io/autamus/picard:latest
```

or to download a specific version of picard run,

```bash
docker pull ghcr.io/autamus/picard:2.24.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/picard picard --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/picard bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the picard container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/picard picard /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC picard container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-picard/).
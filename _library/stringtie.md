---
layout: container
name: stringtie
github: https://github.com/autamus/registry/blob/main/containers/s/stringtie/spack.yaml
versions:
- 1.3.4
- 2.1.6
- 2.1.7
updated_at: 2021-11-17T16:15:51.616844209Z
size: 106MB
description: StringTie is a fast and highly efficient assembler of RNA-Seq alignments
  into potential transcripts.
container_url: https://github.com/orgs/autamus/packages/container/package/stringtie

---
# stringtie
```bash 
Download        : docker pull ghcr.io/autamus/stringtie
Compressed Size : 106MB
```

## Description
StringTie is a fast and highly efficient assembler of RNA-Seq alignments into potential transcripts.

## Usage
### Pull (Download)
To download the latest version of stringtie run,

```bash
docker pull ghcr.io/autamus/stringtie:latest
```

or to download a specific version of stringtie run,

```bash
docker pull ghcr.io/autamus/stringtie:1.3.4
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/stringtie stringtie --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/stringtie bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the stringtie container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/stringtie stringtie /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC stringtie container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-stringtie/).
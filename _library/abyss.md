---
layout: container
name: abyss
github: https://github.com/autamus/registry/blob/main/containers/a/abyss/spack.yaml
versions:
- 2.2.5
- 2.3.0
- 2.3.1
- 2.3.2
updated_at: 2021-11-01T15:53:56.829236826Z
size: 80MB
description: ABySS is a de novo, parallel, paired-end sequence assembler that is designed
  for short reads. The single-processor version is useful for assembling genomes up
  to 100 Mbases in size.
container_url: https://github.com/orgs/autamus/packages/container/package/abyss

---
# abyss
```bash 
Download        : docker pull ghcr.io/autamus/abyss
Compressed Size : 80MB
```

## Description
ABySS is a de novo, parallel, paired-end sequence assembler that is designed for short reads. The single-processor version is useful for assembling genomes up to 100 Mbases in size.

## Usage
### Pull (Download)
To download the latest version of abyss run,

```bash
docker pull ghcr.io/autamus/abyss:latest
```

or to download a specific version of abyss run,

```bash
docker pull ghcr.io/autamus/abyss:2.2.5
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/abyss abyss --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/abyss bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the abyss container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/abyss abyss /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC abyss container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-abyss/).
---
layout: container
name: cloc
github: https://github.com/autamus/registry/blob/main/containers/c/cloc/spack.yaml
versions:
- "1.84"
- "1.88"
- "1.90"
updated_at: 2022-04-02T15:30:30.606195601Z
size: 48MB
description: Count, or compute differences of, physical lines of source code in the
  given files (may be archives such as compressed tarballs or zip files) and/or recursively
  below the given directories.
container_url: https://github.com/orgs/autamus/packages/container/package/cloc

---
# cloc
```bash 
Download        : docker pull ghcr.io/autamus/cloc
Compressed Size : 48MB
```

## Description
Count, or compute differences of, physical lines of source code in the given files (may be archives such as compressed tarballs or zip files) and/or recursively below the given directories.

## Usage
### Pull (Download)
To download the latest version of cloc run,

```bash
docker pull ghcr.io/autamus/cloc:latest
```

or to download a specific version of cloc run,

```bash
docker pull ghcr.io/autamus/cloc:1.84
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/cloc cloc --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/cloc bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the cloc container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/cloc cloc /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC cloc container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-cloc/).
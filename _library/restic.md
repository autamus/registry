---
layout: container
name: restic
github: https://github.com/autamus/registry/blob/main/containers/r/restic/spack.yaml
versions:
- 0.12.1
updated_at: 2022-11-02T23:49:15.720270394Z
size: 34MB
description: Fast, secure, efficient backup program.
container_url: https://github.com/orgs/autamus/packages/container/package/restic

---
# restic
```bash 
Download        : docker pull ghcr.io/autamus/restic
Compressed Size : 34MB
```

## Description
Fast, secure, efficient backup program.

## Usage
### Pull (Download)
To download the latest version of restic run,

```bash
docker pull ghcr.io/autamus/restic:latest
```

or to download a specific version of restic run,

```bash
docker pull ghcr.io/autamus/restic:0.12.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/restic restic --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/restic bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the restic container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/restic restic /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC restic container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-restic/).
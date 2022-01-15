---
layout: container
name: ant
github: https://github.com/autamus/registry/blob/main/containers/a/ant/spack.yaml
versions:
- 1.10.7
updated_at: 2022-01-15T15:42:26.138858089Z
size: 221MB
description: 'Apache Ant is a Java library and command-line tool whose mission is
  to drive processes described in build files as targets and extension points dependent
  upon each other '
container_url: https://github.com/orgs/autamus/packages/container/package/ant

---
# ant
```bash 
Download        : docker pull ghcr.io/autamus/ant
Compressed Size : 221MB
```

## Description
Apache Ant is a Java library and command-line tool whose mission is to drive processes described in build files as targets and extension points dependent upon each other 

## Usage
### Pull (Download)
To download the latest version of ant run,

```bash
docker pull ghcr.io/autamus/ant:latest
```

or to download a specific version of ant run,

```bash
docker pull ghcr.io/autamus/ant:1.10.7
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/ant ant --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/ant bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the ant container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/ant ant /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC ant container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-ant/).
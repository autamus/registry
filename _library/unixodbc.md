---
layout: container
name: unixodbc
github: https://github.com/autamus/registry/blob/main/containers/u/unixodbc/spack.yaml
versions:
- 2.3.4
updated_at: 2022-08-01T20:20:19.30718062Z
size: 29MB
description: ODBC is an open specification for providing application developers with
  a predictable API with which to access Data Sources. Data Sources include SQL Servers
  and any Data Source with an ODBC Driver.
container_url: https://github.com/orgs/autamus/packages/container/package/unixodbc

---
# unixodbc
```bash 
Download        : docker pull ghcr.io/autamus/unixodbc
Compressed Size : 29MB
```

## Description
ODBC is an open specification for providing application developers with a predictable API with which to access Data Sources. Data Sources include SQL Servers and any Data Source with an ODBC Driver.

## Usage
### Pull (Download)
To download the latest version of unixodbc run,

```bash
docker pull ghcr.io/autamus/unixodbc:latest
```

or to download a specific version of unixodbc run,

```bash
docker pull ghcr.io/autamus/unixodbc:2.3.4
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/unixodbc unixodbc --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/unixodbc bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the unixodbc container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/unixodbc unixodbc /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC unixodbc container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-unixodbc/).
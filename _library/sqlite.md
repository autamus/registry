---
layout: container
name: sqlite
github: https://github.com/autamus/registry/blob/main/containers/s/sqlite/spack.yaml
versions:
- 3.35.5
- 3.36.0
- 3.37.1
- 3.37.2
- 3.38.3
- 3.38.5
- 3.39.2
- 3.39.4
updated_at: 2022-10-23T18:24:20.399375046Z
size: 32MB
description: 'SQLite3 is an SQL database engine in a C library. Programs that link
  the SQLite3 library can have SQL database access without running a separate RDBMS
  process. '
container_url: https://github.com/orgs/autamus/packages/container/package/sqlite

---
# sqlite
```bash 
Download        : docker pull ghcr.io/autamus/sqlite
Compressed Size : 32MB
```

## Description
SQLite3 is an SQL database engine in a C library. Programs that link the SQLite3 library can have SQL database access without running a separate RDBMS process. 

## Usage
### Pull (Download)
To download the latest version of sqlite run,

```bash
docker pull ghcr.io/autamus/sqlite:latest
```

or to download a specific version of sqlite run,

```bash
docker pull ghcr.io/autamus/sqlite:3.35.5
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/sqlite sqlite --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/sqlite bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the sqlite container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/sqlite sqlite /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC sqlite container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-sqlite/).
---
layout: container
name: mercurial
github: https://github.com/autamus/registry/blob/main/containers/m/mercurial/spack.yaml
versions:
- "5.8"
updated_at: 2021-11-13T18:58:38.426917025Z
size: 94MB
description: Mercurial is a free, distributed source control management tool.
container_url: https://github.com/orgs/autamus/packages/container/package/mercurial

---
# mercurial
```bash 
Download        : docker pull ghcr.io/autamus/mercurial
Compressed Size : 94MB
```

## Description
Mercurial is a free, distributed source control management tool.

## Usage
### Pull (Download)
To download the latest version of mercurial run,

```bash
docker pull ghcr.io/autamus/mercurial:latest
```

or to download a specific version of mercurial run,

```bash
docker pull ghcr.io/autamus/mercurial:5.8
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/mercurial mercurial --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/mercurial bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the mercurial container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/mercurial mercurial /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC mercurial container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-mercurial/).
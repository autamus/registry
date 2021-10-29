---
layout: container
name: bismark
github: https://github.com/autamus/registry/blob/main/containers/b/bismark/spack.yaml
versions:
- 0.23.0
- 0.23.1
updated_at: 2021-10-29T14:58:39.938951373Z
size: 110MB
description: A tool to map bisulfite converted sequence reads and determine cytosine
  methylation states
container_url: https://github.com/orgs/autamus/packages/container/package/bismark

---
# bismark
```bash 
Download        : docker pull ghcr.io/autamus/bismark
Compressed Size : 110MB
```

## Description
A tool to map bisulfite converted sequence reads and determine cytosine methylation states

## Usage
### Pull (Download)
To download the latest version of bismark run,

```bash
docker pull ghcr.io/autamus/bismark:latest
```

or to download a specific version of bismark run,

```bash
docker pull ghcr.io/autamus/bismark:0.23.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/bismark bismark --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/bismark bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the bismark container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/bismark bismark /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC bismark container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-bismark/).
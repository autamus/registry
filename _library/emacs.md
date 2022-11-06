---
layout: container
name: emacs
github: https://github.com/autamus/registry/blob/main/containers/e/emacs/spack.yaml
versions:
- "27.2"
- "28.1"
updated_at: 2022-11-06T19:25:39.4609346Z
size: 86MB
description: The Emacs programmable text editor.
container_url: https://github.com/orgs/autamus/packages/container/package/emacs

---
# emacs
```bash 
Download        : docker pull ghcr.io/autamus/emacs
Compressed Size : 86MB
```

## Description
The Emacs programmable text editor.

## Usage
### Pull (Download)
To download the latest version of emacs run,

```bash
docker pull ghcr.io/autamus/emacs:latest
```

or to download a specific version of emacs run,

```bash
docker pull ghcr.io/autamus/emacs:27.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/emacs emacs --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/emacs bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the emacs container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/emacs emacs /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC emacs container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-emacs/).
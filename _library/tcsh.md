---
layout: container
name: tcsh
github: https://github.com/autamus/registry/blob/main/containers/t/tcsh/spack.yaml
versions:
- 6.22.02
- 6.24.00
updated_at: 2022-05-29T19:44:03.68495328Z
size: 29MB
description: Tcsh is an enhanced but completely compatible version of csh, the C shell.
  Tcsh is a command language interpreter which can be used both as an interactive
  login shell and as a shell script command processor. Tcsh includes a command line
  editor, programmable word completion, spelling correction, a history mechanism,
  job control and a C language like syntax.
container_url: https://github.com/orgs/autamus/packages/container/package/tcsh

---
# tcsh
```bash 
Download        : docker pull ghcr.io/autamus/tcsh
Compressed Size : 29MB
```

## Description
Tcsh is an enhanced but completely compatible version of csh, the C shell. Tcsh is a command language interpreter which can be used both as an interactive login shell and as a shell script command processor. Tcsh includes a command line editor, programmable word completion, spelling correction, a history mechanism, job control and a C language like syntax.

## Usage
### Pull (Download)
To download the latest version of tcsh run,

```bash
docker pull ghcr.io/autamus/tcsh:latest
```

or to download a specific version of tcsh run,

```bash
docker pull ghcr.io/autamus/tcsh:6.22.02
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/tcsh tcsh --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/tcsh bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the tcsh container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/tcsh tcsh /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC tcsh container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-tcsh/).
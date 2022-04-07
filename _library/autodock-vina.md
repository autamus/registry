---
layout: container
name: autodock-vina
github: https://github.com/autamus/registry/blob/main/containers/a/autodock-vina/spack.yaml
versions:
- 1.1.2
updated_at: 2022-04-07T16:13:18.499380568Z
size: 45MB
description: AutoDock Vina is an open-source program for doing molecular docking
container_url: https://github.com/orgs/autamus/packages/container/package/autodock-vina

---
# autodock-vina
```bash 
Download        : docker pull ghcr.io/autamus/autodock-vina
Compressed Size : 45MB
```

## Description
AutoDock Vina is an open-source program for doing molecular docking

## Usage
### Pull (Download)
To download the latest version of autodock-vina run,

```bash
docker pull ghcr.io/autamus/autodock-vina:latest
```

or to download a specific version of autodock-vina run,

```bash
docker pull ghcr.io/autamus/autodock-vina:1.1.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/autodock-vina autodock-vina --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/autodock-vina bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the autodock-vina container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/autodock-vina autodock-vina /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC autodock-vina container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-autodock-vina/).
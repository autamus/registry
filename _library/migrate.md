---
layout: container
name: migrate
github: https://github.com/autamus/registry/blob/main/containers/m/migrate/spack.yaml
versions:
- 3.7.2
updated_at: 2021-09-20T14:44:58.644311774Z
size: 27MB
description: Migrate estimates effective population sizes and past migration rates
  between n population assuming a migration matrix model with asymmetric migration
  rates and different subpopulation sizes
container_url: https://github.com/orgs/autamus/packages/container/package/migrate

---
# migrate
```bash 
Download        : docker pull ghcr.io/autamus/migrate
Compressed Size : 27MB
```

## Description
Migrate estimates effective population sizes and past migration rates between n population assuming a migration matrix model with asymmetric migration rates and different subpopulation sizes

## Usage
### Pull (Download)
To download the latest version of migrate run,

```bash
docker pull ghcr.io/autamus/migrate:latest
```

or to download a specific version of migrate run,

```bash
docker pull ghcr.io/autamus/migrate:3.7.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/migrate migrate --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/migrate bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the migrate container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/migrate migrate /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC migrate container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-migrate/).
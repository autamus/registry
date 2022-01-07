---
layout: container
name: rust
github: https://github.com/autamus/registry/blob/main/containers/r/rust/spack.yaml
versions:
- 1.51.0
- 1.52.1
- 1.53.0
- 1.54.0
updated_at: 2022-01-07T16:26:25.064735074Z
size: 255MB
description: .format( cargo=join_path(boot_bin, 'cargo
container_url: https://github.com/orgs/autamus/packages/container/package/rust

---
# rust
```bash 
Download        : docker pull ghcr.io/autamus/rust
Compressed Size : 255MB
```

## Description
.format( cargo=join_path(boot_bin, 'cargo

## Usage
### Pull (Download)
To download the latest version of rust run,

```bash
docker pull ghcr.io/autamus/rust:latest
```

or to download a specific version of rust run,

```bash
docker pull ghcr.io/autamus/rust:1.51.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/rust rust --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/rust bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the rust container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/rust rust /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC rust container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-rust/).
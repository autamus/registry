---
layout: container
name: abi-dumper
github: https://github.com/autamus/registry/blob/main/containers/a/abi-dumper/spack.yaml
versions:
- "1.1"
- "1.2"
updated_at: 2022-08-07T16:04:39.133240309Z
size: 136MB
description: ABI Dumper is a tool to dump ABI of an ELF object containing DWARF debug
  info.
container_url: https://github.com/orgs/autamus/packages/container/package/abi-dumper

---
# abi-dumper
```bash 
Download        : docker pull ghcr.io/autamus/abi-dumper
Compressed Size : 136MB
```

## Description
ABI Dumper is a tool to dump ABI of an ELF object containing DWARF debug info.

## Usage
### Pull (Download)
To download the latest version of abi-dumper run,

```bash
docker pull ghcr.io/autamus/abi-dumper:latest
```

or to download a specific version of abi-dumper run,

```bash
docker pull ghcr.io/autamus/abi-dumper:1.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/abi-dumper abi-dumper --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/abi-dumper bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the abi-dumper container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/abi-dumper abi-dumper /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC abi-dumper container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-abi-dumper/).
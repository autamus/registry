---
layout: container
name: addrwatch
github: https://github.com/autamus/registry/blob/main/containers/a/addrwatch/spack.yaml
versions:
- 1.0.2
updated_at: 2021-05-26T02:58:32.123571425Z
size: 31MB
description: A tool similar to arpwatch for IPv4/IPv6 and ethernet address pairing
  monitoring.
container_url: https://github.com/orgs/autamus/packages/container/package/addrwatch

---
# addrwatch
```bash 
Download        : docker pull ghcr.io/autamus/addrwatch
Compressed Size : 31MB
```

## Description
A tool similar to arpwatch for IPv4/IPv6 and ethernet address pairing monitoring.

## Usage
### Pull (Download)
To download the latest version of addrwatch run,

```bash
docker pull ghcr.io/autamus/addrwatch:latest
```

or to download a specific version of addrwatch run,

```bash
docker pull ghcr.io/autamus/addrwatch:1.0.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/addrwatch addrwatch --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/addrwatch bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the addrwatch container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/addrwatch addrwatch /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC addrwatch container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-addrwatch/).
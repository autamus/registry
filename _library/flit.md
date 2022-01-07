---
layout: container
name: flit
github: https://github.com/autamus/registry/blob/main/containers/f/flit/spack.yaml
versions:
- 2.1.0
updated_at: 2022-01-07T16:09:36.887794415Z
size: 87MB
description: Floating-point Litmus Tests (FLiT) is a C++ test infrastructure for detecting
  variability in floating-point code caused by variations in compiler code generation,
  hardware and execution environments.
container_url: https://github.com/orgs/autamus/packages/container/package/flit

---
# flit
```bash 
Download        : docker pull ghcr.io/autamus/flit
Compressed Size : 87MB
```

## Description
Floating-point Litmus Tests (FLiT) is a C++ test infrastructure for detecting variability in floating-point code caused by variations in compiler code generation, hardware and execution environments.

## Usage
### Pull (Download)
To download the latest version of flit run,

```bash
docker pull ghcr.io/autamus/flit:latest
```

or to download a specific version of flit run,

```bash
docker pull ghcr.io/autamus/flit:2.1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/flit flit --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/flit bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the flit container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/flit flit /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC flit container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-flit/).
---
layout: container
name: caliper
github: https://github.com/autamus/registry/blob/main/containers/c/caliper/spack.yaml
versions:
- 2.6.0
- 2.7.0
updated_at: 2022-01-07T16:05:09.038586478Z
size: 72MB
description: 'Caliper is a program instrumentation and performance measurement framework.
  It is designed as a performance analysis toolbox in a library, allowing one to bake
  performance analysis capabilities directly into applications and activate them at
  runtime. '
container_url: https://github.com/orgs/autamus/packages/container/package/caliper

---
# caliper
```bash 
Download        : docker pull ghcr.io/autamus/caliper
Compressed Size : 72MB
```

## Description
Caliper is a program instrumentation and performance measurement framework. It is designed as a performance analysis toolbox in a library, allowing one to bake performance analysis capabilities directly into applications and activate them at runtime. 

## Usage
### Pull (Download)
To download the latest version of caliper run,

```bash
docker pull ghcr.io/autamus/caliper:latest
```

or to download a specific version of caliper run,

```bash
docker pull ghcr.io/autamus/caliper:2.6.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/caliper caliper --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/caliper bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the caliper container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/caliper caliper /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC caliper container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-caliper/).
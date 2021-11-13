---
layout: container
name: benchmark
github: https://github.com/autamus/registry/blob/main/containers/b/benchmark/spack.yaml
versions:
- 1.5.5
- 1.5.6
- 1.6.0
updated_at: 2021-11-13T18:44:47.770529641Z
size: 27MB
description: A microbenchmark support library
container_url: https://github.com/orgs/autamus/packages/container/package/benchmark

---
# benchmark
```bash 
Download        : docker pull ghcr.io/autamus/benchmark
Compressed Size : 27MB
```

## Description
A microbenchmark support library

## Usage
### Pull (Download)
To download the latest version of benchmark run,

```bash
docker pull ghcr.io/autamus/benchmark:latest
```

or to download a specific version of benchmark run,

```bash
docker pull ghcr.io/autamus/benchmark:1.5.5
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/benchmark benchmark --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/benchmark bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the benchmark container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/benchmark benchmark /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC benchmark container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-benchmark/).
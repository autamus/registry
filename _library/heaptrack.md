---
layout: container
name: heaptrack
github: https://github.com/autamus/registry/blob/main/containers/h/heaptrack/spack.yaml
versions:
- 1.1.0
- 1.2.0
updated_at: 2021-10-29T15:02:08.17292657Z
size: 65MB
description: 'Heaptrack is a heap memory profiler that traces all memory allocations
  and annotates these events with stack traces. '
container_url: https://github.com/orgs/autamus/packages/container/package/heaptrack

---
# heaptrack
```bash 
Download        : docker pull ghcr.io/autamus/heaptrack
Compressed Size : 65MB
```

## Description
Heaptrack is a heap memory profiler that traces all memory allocations and annotates these events with stack traces. 

## Usage
### Pull (Download)
To download the latest version of heaptrack run,

```bash
docker pull ghcr.io/autamus/heaptrack:latest
```

or to download a specific version of heaptrack run,

```bash
docker pull ghcr.io/autamus/heaptrack:1.1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/heaptrack heaptrack --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/heaptrack bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the heaptrack container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/heaptrack heaptrack /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC heaptrack container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-heaptrack/).
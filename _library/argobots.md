---
layout: container
name: argobots
github: https://github.com/autamus/registry/blob/main/containers/a/argobots/spack.yaml
versions:
- "1.0"
- "1.1"
updated_at: 2022-03-22T14:46:22.342927032Z
size: 27MB
description: 'Argobots, which was developed as a part of the Argo project, is a lightweight
  runtime system that supports integrated computation and data movement with massive
  concurrency. It will directly leverage the lowest-level constructs in the hardware
  and OS: lightweight notification mechanisms, data movement engines, memory mapping,
  and data placement strategies. It consists of an execution model and a memory model.'
container_url: https://github.com/orgs/autamus/packages/container/package/argobots

---
# argobots
```bash 
Download        : docker pull ghcr.io/autamus/argobots
Compressed Size : 27MB
```

## Description
Argobots, which was developed as a part of the Argo project, is a lightweight runtime system that supports integrated computation and data movement with massive concurrency. It will directly leverage the lowest-level constructs in the hardware and OS: lightweight notification mechanisms, data movement engines, memory mapping, and data placement strategies. It consists of an execution model and a memory model.

## Usage
### Pull (Download)
To download the latest version of argobots run,

```bash
docker pull ghcr.io/autamus/argobots:latest
```

or to download a specific version of argobots run,

```bash
docker pull ghcr.io/autamus/argobots:1.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/argobots argobots --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/argobots bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the argobots container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/argobots argobots /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC argobots container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-argobots/).
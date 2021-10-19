---
layout: container
name: dyninst
github: https://github.com/autamus/registry/blob/main/containers/d/dyninst/spack.yaml
versions:
- 11.0.0
- 11.0.1
updated_at: 2021-10-19T07:24:58.924920411Z
size: 70MB
description: API for dynamic binary instrumentation. Modify programs while they are
  executing without recompiling, re-linking, or re-executing.
container_url: https://github.com/orgs/autamus/packages/container/package/dyninst

---
# dyninst
```bash 
Download        : docker pull ghcr.io/autamus/dyninst
Compressed Size : 70MB
```

## Description
API for dynamic binary instrumentation. Modify programs while they are executing without recompiling, re-linking, or re-executing.

## Usage
### Pull (Download)
To download the latest version of dyninst run,

```bash
docker pull ghcr.io/autamus/dyninst:latest
```

or to download a specific version of dyninst run,

```bash
docker pull ghcr.io/autamus/dyninst:11.0.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/dyninst dyninst --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/dyninst bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the dyninst container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/dyninst dyninst /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC dyninst container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-dyninst/).
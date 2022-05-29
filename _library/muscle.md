---
layout: container
name: muscle
github: https://github.com/autamus/registry/blob/main/containers/m/muscle/spack.yaml
versions:
- 3.8.1551
updated_at: 2022-05-29T18:48:29.642156649Z
size: 27MB
description: MUSCLE is one of the best-performing multiple alignment programs according
  to published benchmark tests, with accuracy and speed that are consistently better
  than CLUSTALW.
container_url: https://github.com/orgs/autamus/packages/container/package/muscle

---
# muscle
```bash 
Download        : docker pull ghcr.io/autamus/muscle
Compressed Size : 27MB
```

## Description
MUSCLE is one of the best-performing multiple alignment programs according to published benchmark tests, with accuracy and speed that are consistently better than CLUSTALW.

## Usage
### Pull (Download)
To download the latest version of muscle run,

```bash
docker pull ghcr.io/autamus/muscle:latest
```

or to download a specific version of muscle run,

```bash
docker pull ghcr.io/autamus/muscle:3.8.1551
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/muscle muscle --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/muscle bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the muscle container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/muscle muscle /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC muscle container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-muscle/).
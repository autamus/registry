---
layout: container
name: zfp
github: https://github.com/autamus/registry/blob/main/containers/z/zfp/spack.yaml
versions:
- 0.5.5
updated_at: 2022-01-07T16:29:21.595482891Z
size: 27MB
description: 'zfp is a compressed number format for multidimensional floating-point
  and integer arrays. zfp provides compressed-array classes that support high throughput
  read and write random access to individual array elements. zfp also supports serial
  and parallel (OpenMP and CUDA) compression of whole arrays. '
container_url: https://github.com/orgs/autamus/packages/container/package/zfp

---
# zfp
```bash 
Download        : docker pull ghcr.io/autamus/zfp
Compressed Size : 27MB
```

## Description
zfp is a compressed number format for multidimensional floating-point and integer arrays. zfp provides compressed-array classes that support high throughput read and write random access to individual array elements. zfp also supports serial and parallel (OpenMP and CUDA) compression of whole arrays. 

## Usage
### Pull (Download)
To download the latest version of zfp run,

```bash
docker pull ghcr.io/autamus/zfp:latest
```

or to download a specific version of zfp run,

```bash
docker pull ghcr.io/autamus/zfp:0.5.5
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/zfp zfp --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/zfp bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the zfp container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/zfp zfp /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC zfp container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-zfp/).
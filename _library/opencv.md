---
layout: container
name: opencv
github: https://github.com/autamus/registry/blob/main/containers/o/opencv/spack.yaml
versions:
- 4.5.2
- 4.5.3
updated_at: 2021-10-19T07:40:33.043952683Z
size: 30MB
description: OpenCV (Open Source Computer Vision Library) is an open source computer
  vision and machine learning software library.
container_url: https://github.com/orgs/autamus/packages/container/package/opencv

---
# opencv
```bash 
Download        : docker pull ghcr.io/autamus/opencv
Compressed Size : 30MB
```

## Description
OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.

## Usage
### Pull (Download)
To download the latest version of opencv run,

```bash
docker pull ghcr.io/autamus/opencv:latest
```

or to download a specific version of opencv run,

```bash
docker pull ghcr.io/autamus/opencv:4.5.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/opencv opencv --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/opencv bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the opencv container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/opencv opencv /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC opencv container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-opencv/).
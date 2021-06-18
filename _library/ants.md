---
layout: container
name: ants
github: https://github.com/autamus/registry/blob/main/containers/a/ants/spack.yaml
versions:
- 2.3.5
updated_at: 2021-06-18T02:03:07.938405851Z
size: 563MB
description: 'ANTs extracts information from complex datasets that include imaging.
  Paired with ANTsR (answer), ANTs is useful for managing, interpreting and visualizing
  multidimensional data. ANTs is popularly considered a state-of-the-art medical image
  registration and segmentation toolkit. ANTs depends on the Insight ToolKit (ITK),
  a widely used medical image processing library to which ANTs developers contribute. '
container_url: https://github.com/orgs/autamus/packages/container/package/ants

---
# ants
```bash 
Download        : docker pull ghcr.io/autamus/ants
Compressed Size : 563MB
```

## Description
ANTs extracts information from complex datasets that include imaging. Paired with ANTsR (answer), ANTs is useful for managing, interpreting and visualizing multidimensional data. ANTs is popularly considered a state-of-the-art medical image registration and segmentation toolkit. ANTs depends on the Insight ToolKit (ITK), a widely used medical image processing library to which ANTs developers contribute. 

## Usage
### Pull (Download)
To download the latest version of ants run,

```bash
docker pull ghcr.io/autamus/ants:latest
```

or to download a specific version of ants run,

```bash
docker pull ghcr.io/autamus/ants:2.3.5
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/ants ants --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/ants bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the ants container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/ants ants /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC ants container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-ants/).
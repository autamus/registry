---
layout: container
name: povray
github: https://github.com/autamus/registry/blob/main/containers/p/povray/spack.yaml
versions:
- 3.7.0.10
- 3.7.0.8
- 3.7.0.9
updated_at: 2022-11-06T20:48:01.99902144Z
size: 1141MB
description: 'The Persistence of Vision Raytracer creates three-dimensional, photo-realistic
  images using a rendering technique called ray-tracing. It reads in a text file containing
  information describing the objects and lighting in a scene and generates an image
  of that scene from the view point of a camera also described in the text file. Ray-tracing
  is not a fast process by any means, but it produces very high quality images with
  realistic reflections, shading, perspective and other effects. '
container_url: https://github.com/orgs/autamus/packages/container/package/povray

---
# povray
```bash 
Download        : docker pull ghcr.io/autamus/povray
Compressed Size : 1141MB
```

## Description
The Persistence of Vision Raytracer creates three-dimensional, photo-realistic images using a rendering technique called ray-tracing. It reads in a text file containing information describing the objects and lighting in a scene and generates an image of that scene from the view point of a camera also described in the text file. Ray-tracing is not a fast process by any means, but it produces very high quality images with realistic reflections, shading, perspective and other effects. 

## Usage
### Pull (Download)
To download the latest version of povray run,

```bash
docker pull ghcr.io/autamus/povray:latest
```

or to download a specific version of povray run,

```bash
docker pull ghcr.io/autamus/povray:3.7.0.10
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/povray povray --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/povray bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the povray container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/povray povray /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC povray container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-povray/).
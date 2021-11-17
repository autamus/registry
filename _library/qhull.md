---
layout: container
name: qhull
github: https://github.com/autamus/registry/blob/main/containers/q/qhull/spack.yaml
versions:
- "2020.1"
- "2020.2"
updated_at: 2021-11-17T16:08:11.887850464Z
size: 29MB
description: Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
  halfspace intersection about a point, furt hest-site Delaunay triangulation, and
  furthest-site Voronoi diagram. The source code runs in 2-d, 3-d, 4-d, and higher
  dimensions. Qhull implements the Quickhull algorithm for computing the convex hull.
  It handles roundoff errors from floating point arithmetic. It computes volumes,
  surface areas, and approximations to the convex hull.
container_url: https://github.com/orgs/autamus/packages/container/package/qhull

---
# qhull
```bash 
Download        : docker pull ghcr.io/autamus/qhull
Compressed Size : 29MB
```

## Description
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram, halfspace intersection about a point, furt hest-site Delaunay triangulation, and furthest-site Voronoi diagram. The source code runs in 2-d, 3-d, 4-d, and higher dimensions. Qhull implements the Quickhull algorithm for computing the convex hull. It handles roundoff errors from floating point arithmetic. It computes volumes, surface areas, and approximations to the convex hull.

## Usage
### Pull (Download)
To download the latest version of qhull run,

```bash
docker pull ghcr.io/autamus/qhull:latest
```

or to download a specific version of qhull run,

```bash
docker pull ghcr.io/autamus/qhull:2020.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/qhull qhull --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/qhull bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the qhull container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/qhull qhull /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC qhull container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-qhull/).
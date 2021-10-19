---
layout: container
name: omega-h
github: https://github.com/autamus/registry/blob/main/containers/o/omega-h/spack.yaml
versions:
- 9.32.5
- 9.33.3
- 9.34.1
- 9.34.5
updated_at: 2021-10-19T07:42:45.028606047Z
size: 109MB
description: 'Omega_h is a C++11 library providing data structures and algorithms
  for adaptive discretizations. Its specialty is anisotropic triangle and tetrahedral
  mesh adaptation. It runs efficiently on most modern HPC hardware including GPUs. '
container_url: https://github.com/orgs/autamus/packages/container/package/omega-h

---
# omega-h
```bash 
Download        : docker pull ghcr.io/autamus/omega-h
Compressed Size : 109MB
```

## Description
Omega_h is a C++11 library providing data structures and algorithms for adaptive discretizations. Its specialty is anisotropic triangle and tetrahedral mesh adaptation. It runs efficiently on most modern HPC hardware including GPUs. 

## Usage
### Pull (Download)
To download the latest version of omega-h run,

```bash
docker pull ghcr.io/autamus/omega-h:latest
```

or to download a specific version of omega-h run,

```bash
docker pull ghcr.io/autamus/omega-h:9.32.5
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/omega-h omega-h --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/omega-h bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the omega-h container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/omega-h omega-h /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC omega-h container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-omega-h/).
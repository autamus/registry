---
layout: container
name: nco
github: https://github.com/autamus/registry/blob/main/containers/n/nco/spack.yaml
versions:
- 4.9.3
- 4.9.7
- 4.9.8
- 4.9.9
- 5.0.0
- 5.0.1
- 5.0.3
updated_at: 2021-10-29T15:11:18.247941928Z
size: 88MB
description: The NCO toolkit manipulates and analyzes data stored in netCDF-accessible
  formats
container_url: https://github.com/orgs/autamus/packages/container/package/nco

---
# nco
```bash 
Download        : docker pull ghcr.io/autamus/nco
Compressed Size : 88MB
```

## Description
The NCO toolkit manipulates and analyzes data stored in netCDF-accessible formats

## Usage
### Pull (Download)
To download the latest version of nco run,

```bash
docker pull ghcr.io/autamus/nco:latest
```

or to download a specific version of nco run,

```bash
docker pull ghcr.io/autamus/nco:4.9.3
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/nco nco --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/nco bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the nco container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/nco nco /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC nco container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-nco/).
---
layout: container
name: parallel-netcdf
github: https://github.com/autamus/registry/blob/main/containers/p/parallel-netcdf/spack.yaml
versions:
- 1.12.2
- 1.12.3
updated_at: 2022-11-03T20:28:28.573577416Z
size: 65MB
description: 'PnetCDF (Parallel netCDF) is a high-performance parallel I/O library
  for accessing files in format compatibility with Unidata''s NetCDF, specifically
  the formats of CDF-1, 2, and 5. '
container_url: https://github.com/orgs/autamus/packages/container/package/parallel-netcdf

---
# parallel-netcdf
```bash 
Download        : docker pull ghcr.io/autamus/parallel-netcdf
Compressed Size : 65MB
```

## Description
PnetCDF (Parallel netCDF) is a high-performance parallel I/O library for accessing files in format compatibility with Unidata's NetCDF, specifically the formats of CDF-1, 2, and 5. 

## Usage
### Pull (Download)
To download the latest version of parallel-netcdf run,

```bash
docker pull ghcr.io/autamus/parallel-netcdf:latest
```

or to download a specific version of parallel-netcdf run,

```bash
docker pull ghcr.io/autamus/parallel-netcdf:1.12.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/parallel-netcdf parallel-netcdf --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/parallel-netcdf bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the parallel-netcdf container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/parallel-netcdf parallel-netcdf /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC parallel-netcdf container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-parallel-netcdf/).
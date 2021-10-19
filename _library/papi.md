---
layout: container
name: papi
github: https://github.com/autamus/registry/blob/main/containers/p/papi/spack.yaml
versions:
- 6.0.0.1
updated_at: 2021-10-19T07:41:18.123263466Z
size: 35MB
description: PAPI provides the tool designer and application engineer with a consistent
  interface and methodology for use of the performance counter hardware found in most
  major microprocessors. PAPI enables software engineers to see, in near real time,
  the relation between software performance and processor events. In addition Component
  PAPI provides access to a collection of components that expose performance measurement
  opportunities across the hardware and software stack.
container_url: https://github.com/orgs/autamus/packages/container/package/papi

---
# papi
```bash 
Download        : docker pull ghcr.io/autamus/papi
Compressed Size : 35MB
```

## Description
PAPI provides the tool designer and application engineer with a consistent interface and methodology for use of the performance counter hardware found in most major microprocessors. PAPI enables software engineers to see, in near real time, the relation between software performance and processor events. In addition Component PAPI provides access to a collection of components that expose performance measurement opportunities across the hardware and software stack.

## Usage
### Pull (Download)
To download the latest version of papi run,

```bash
docker pull ghcr.io/autamus/papi:latest
```

or to download a specific version of papi run,

```bash
docker pull ghcr.io/autamus/papi:6.0.0.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/papi papi --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/papi bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the papi container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/papi papi /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC papi container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-papi/).
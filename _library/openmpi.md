---
layout: container
name: openmpi
github: https://github.com/autamus/registry/blob/main/containers/o/openmpi/spack.yaml
versions:
- 4.1.1
- 4.1.2
updated_at: 2022-01-04T05:44:53.458335601Z
size: 52MB
description: 'An open source Message Passing Interface implementation. The Open MPI
  Project is an open source Message Passing Interface implementation that is developed
  and maintained by a consortium of academic, research, and industry partners. Open
  MPI is therefore able to combine the expertise, technologies, and resources from
  all across the High Performance Computing community in order to build the best MPI
  library available. Open MPI offers advantages for system and software vendors, application
  developers and computer science researchers. '
container_url: https://github.com/orgs/autamus/packages/container/package/openmpi

---
# openmpi
```bash 
Download        : docker pull ghcr.io/autamus/openmpi
Compressed Size : 52MB
```

## Description
An open source Message Passing Interface implementation. The Open MPI Project is an open source Message Passing Interface implementation that is developed and maintained by a consortium of academic, research, and industry partners. Open MPI is therefore able to combine the expertise, technologies, and resources from all across the High Performance Computing community in order to build the best MPI library available. Open MPI offers advantages for system and software vendors, application developers and computer science researchers. 

## Usage
### Pull (Download)
To download the latest version of openmpi run,

```bash
docker pull ghcr.io/autamus/openmpi:latest
```

or to download a specific version of openmpi run,

```bash
docker pull ghcr.io/autamus/openmpi:4.1.1
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/openmpi openmpi --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/openmpi bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the openmpi container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/openmpi openmpi /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC openmpi container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-openmpi/).
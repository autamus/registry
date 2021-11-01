---
layout: container
name: hpctoolkit
github: https://github.com/autamus/registry/blob/main/containers/h/hpctoolkit/spack.yaml
versions:
- 2021.05.15
- 2021.10.15
updated_at: 2021-11-01T16:05:50.145055679Z
size: 382MB
description: HPCToolkit is an integrated suite of tools for measurement and analysis
  of program performance on computers ranging from multicore desktop systems to the
  nation's largest supercomputers. By using statistical sampling of timers and hardware
  performance counters, HPCToolkit collects accurate measurements of a program's work,
  resource consumption, and inefficiency and attributes them to the full calling context
  in which they occur.
container_url: https://github.com/orgs/autamus/packages/container/package/hpctoolkit

---
# hpctoolkit
```bash 
Download        : docker pull ghcr.io/autamus/hpctoolkit
Compressed Size : 382MB
```

## Description
HPCToolkit is an integrated suite of tools for measurement and analysis of program performance on computers ranging from multicore desktop systems to the nation's largest supercomputers. By using statistical sampling of timers and hardware performance counters, HPCToolkit collects accurate measurements of a program's work, resource consumption, and inefficiency and attributes them to the full calling context in which they occur.

## Usage
### Pull (Download)
To download the latest version of hpctoolkit run,

```bash
docker pull ghcr.io/autamus/hpctoolkit:latest
```

or to download a specific version of hpctoolkit run,

```bash
docker pull ghcr.io/autamus/hpctoolkit:2021.05.15
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/hpctoolkit hpctoolkit --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/hpctoolkit bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the hpctoolkit container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/hpctoolkit hpctoolkit /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC hpctoolkit container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-hpctoolkit/).
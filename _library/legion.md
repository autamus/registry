---
layout: container
name: legion
github: https://github.com/autamus/registry/blob/main/containers/l/legion/spack.yaml
versions:
- 21.03.0
updated_at: 2022-11-05T21:28:48.804717713Z
size: 32MB
description: Legion is a data-centric parallel programming system for writing portable
  high performance programs targeted at distributed heterogeneous architectures. Legion
  presents abstractions which allow programmers to describe properties of program
  data (e.g. independence, locality). By making the Legion programming system aware
  of the structure of program data, it can automate many of the tedious tasks programmers
  currently face, including correctly extracting task- and data-level parallelism
  and moving data around complex memory hierarchies. A novel mapping interface provides
  explicit programmer controlled placement of data in the memory hierarchy and assignment
  of tasks to processors in a way that is orthogonal to correctness, thereby enabling
  easy porting and tuning of Legion applications to new architectures.
container_url: https://github.com/orgs/autamus/packages/container/package/legion

---
# legion
```bash 
Download        : docker pull ghcr.io/autamus/legion
Compressed Size : 32MB
```

## Description
Legion is a data-centric parallel programming system for writing portable high performance programs targeted at distributed heterogeneous architectures. Legion presents abstractions which allow programmers to describe properties of program data (e.g. independence, locality). By making the Legion programming system aware of the structure of program data, it can automate many of the tedious tasks programmers currently face, including correctly extracting task- and data-level parallelism and moving data around complex memory hierarchies. A novel mapping interface provides explicit programmer controlled placement of data in the memory hierarchy and assignment of tasks to processors in a way that is orthogonal to correctness, thereby enabling easy porting and tuning of Legion applications to new architectures.

## Usage
### Pull (Download)
To download the latest version of legion run,

```bash
docker pull ghcr.io/autamus/legion:latest
```

or to download a specific version of legion run,

```bash
docker pull ghcr.io/autamus/legion:21.03.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/legion legion --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/legion bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the legion container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/legion legion /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC legion container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-legion/).
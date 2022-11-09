---
layout: container
name: clingo
github: https://github.com/autamus/registry/blob/main/containers/c/clingo/spack.yaml
versions:
- 5.4.0
- 5.4.1
- 5.5.0
- 5.5.1
- 5.5.2
updated_at: 2022-11-09T20:50:22.889551053Z
size: 110MB
description: 'Clingo: A grounder and solver for logic programs Clingo is part of the
  Potassco project for Answer Set Programming (ASP). ASP offers a simple and powerful
  modeling language to describe combinatorial problems as logic programs. The clingo
  system then takes such a logic program and computes answer sets representing solutions
  to the given problem.'
container_url: https://github.com/orgs/autamus/packages/container/package/clingo

---
# clingo
```bash 
Download        : docker pull ghcr.io/autamus/clingo
Compressed Size : 110MB
```

## Description
Clingo: A grounder and solver for logic programs Clingo is part of the Potassco project for Answer Set Programming (ASP). ASP offers a simple and powerful modeling language to describe combinatorial problems as logic programs. The clingo system then takes such a logic program and computes answer sets representing solutions to the given problem.

## Usage
### Pull (Download)
To download the latest version of clingo run,

```bash
docker pull ghcr.io/autamus/clingo:latest
```

or to download a specific version of clingo run,

```bash
docker pull ghcr.io/autamus/clingo:5.4.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/clingo clingo --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/clingo bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the clingo container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/clingo clingo /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC clingo container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-clingo/).
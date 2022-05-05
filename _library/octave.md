---
layout: container
name: octave
github: https://github.com/autamus/registry/blob/main/containers/o/octave/spack.yaml
versions:
- 6.2.0
- 6.3.0
- 6.4.0
- 7.1.0
updated_at: 2022-05-05T18:13:38.754252553Z
size: 75MB
description: 'GNU Octave is a high-level language, primarily intended for numerical
  computations. It provides a convenient command line interface for solving linear
  and nonlinear problems numerically, and for performing other numerical experiments
  using a language that is mostly compatible with Matlab. It may also be used as a
  batch-oriented language. '
container_url: https://github.com/orgs/autamus/packages/container/package/octave

---
# octave
```bash 
Download        : docker pull ghcr.io/autamus/octave
Compressed Size : 75MB
```

## Description
GNU Octave is a high-level language, primarily intended for numerical computations. It provides a convenient command line interface for solving linear and nonlinear problems numerically, and for performing other numerical experiments using a language that is mostly compatible with Matlab. It may also be used as a batch-oriented language. 

## Usage
### Pull (Download)
To download the latest version of octave run,

```bash
docker pull ghcr.io/autamus/octave:latest
```

or to download a specific version of octave run,

```bash
docker pull ghcr.io/autamus/octave:6.2.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/octave octave --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/octave bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the octave container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/octave octave /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC octave container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-octave/).
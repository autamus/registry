---
layout: container
name: jags
github: https://github.com/autamus/registry/blob/main/containers/j/jags/spack.yaml
versions:
- 4.3.0
- latest
updated_at: 2022-05-29T18:52:47.986299878Z
size: 51MB
description: JAGS is Just Another Gibbs Sampler. It is a program for analysis of Bayesian
  hierarchical models using Markov Chain Monte Carlo (MCMC) simulation not wholly
  unlike BUGS
container_url: https://github.com/orgs/autamus/packages/container/package/jags

---
# jags
```bash 
Download        : docker pull ghcr.io/autamus/jags
Compressed Size : 51MB
```

## Description
JAGS is Just Another Gibbs Sampler. It is a program for analysis of Bayesian hierarchical models using Markov Chain Monte Carlo (MCMC) simulation not wholly unlike BUGS

## Usage
### Pull (Download)
To download the latest version of jags run,

```bash
docker pull ghcr.io/autamus/jags:latest
```

or to download a specific version of jags run,

```bash
docker pull ghcr.io/autamus/jags:4.3.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/jags jags --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/jags bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the jags container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/jags jags /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC jags container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-jags/).
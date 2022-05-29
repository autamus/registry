---
layout: container
name: beast2
github: https://github.com/autamus/registry/blob/main/containers/b/beast2/spack.yaml
versions:
- 2.6.3
- 2.6.4
- 2.6.6
updated_at: 2022-05-29T17:35:41.022458867Z
size: 227MB
description: BEAST is a cross-platform program for Bayesian inference using MCMC of
  molecular sequences. It is entirely orientated towards rooted, time-measured phylogenies
  inferred using strict or relaxed molecular clock models. It can be used as a method
  of reconstructing phylogenies but is also a framework for testing evolutionary hypotheses
  without conditioning on a single tree topology.
container_url: https://github.com/orgs/autamus/packages/container/package/beast2

---
# beast2
```bash 
Download        : docker pull ghcr.io/autamus/beast2
Compressed Size : 227MB
```

## Description
BEAST is a cross-platform program for Bayesian inference using MCMC of molecular sequences. It is entirely orientated towards rooted, time-measured phylogenies inferred using strict or relaxed molecular clock models. It can be used as a method of reconstructing phylogenies but is also a framework for testing evolutionary hypotheses without conditioning on a single tree topology.

## Usage
### Pull (Download)
To download the latest version of beast2 run,

```bash
docker pull ghcr.io/autamus/beast2:latest
```

or to download a specific version of beast2 run,

```bash
docker pull ghcr.io/autamus/beast2:2.6.3
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/beast2 beast2 --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/beast2 bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the beast2 container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/beast2 beast2 /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC beast2 container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-beast2/).
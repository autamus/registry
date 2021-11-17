---
layout: container
name: dakota
github: https://github.com/autamus/registry/blob/main/containers/d/dakota/spack.yaml
versions:
- "6.12"
updated_at: 2021-11-17T15:56:45.087583749Z
size: 162MB
description: 'The Dakota toolkit provides a flexible, extensible interface between
  analysis codes and iterative systems analysis methods. Dakota contains algorithms
  for: - optimization with gradient and non gradient-based methods; - uncertainty
  quantification with sampling, reliability, stochastic - expansion, and epistemic
  methods; - parameter estimation with nonlinear least squares methods; - sensitivity/variance
  analysis with design of experiments and - parameter study methods. These capabilities
  may be used on their own or as components within advanced strategies such as hybrid
  optimization, surrogate-based optimization, mixed integer nonlinear programming,
  or optimization under uncertainty. '
container_url: https://github.com/orgs/autamus/packages/container/package/dakota

---
# dakota
```bash 
Download        : docker pull ghcr.io/autamus/dakota
Compressed Size : 162MB
```

## Description
The Dakota toolkit provides a flexible, extensible interface between analysis codes and iterative systems analysis methods. Dakota contains algorithms for: - optimization with gradient and non gradient-based methods; - uncertainty quantification with sampling, reliability, stochastic - expansion, and epistemic methods; - parameter estimation with nonlinear least squares methods; - sensitivity/variance analysis with design of experiments and - parameter study methods. These capabilities may be used on their own or as components within advanced strategies such as hybrid optimization, surrogate-based optimization, mixed integer nonlinear programming, or optimization under uncertainty. 

## Usage
### Pull (Download)
To download the latest version of dakota run,

```bash
docker pull ghcr.io/autamus/dakota:latest
```

or to download a specific version of dakota run,

```bash
docker pull ghcr.io/autamus/dakota:6.12
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/dakota dakota --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/dakota bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the dakota container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/dakota dakota /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC dakota container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-dakota/).
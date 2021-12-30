---
layout: container
name: ruby
github: https://github.com/autamus/registry/blob/main/containers/r/ruby/spack.yaml
versions:
- 3.0.0
- 3.0.1
- 3.0.2
- 3.1.0
updated_at: 2021-12-30T15:46:23.480116624Z
size: 46MB
description: A dynamic, open source programming language with a focus on simplicity
  and productivity.
container_url: https://github.com/orgs/autamus/packages/container/package/ruby

---
# ruby
```bash 
Download        : docker pull ghcr.io/autamus/ruby
Compressed Size : 46MB
```

## Description
A dynamic, open source programming language with a focus on simplicity and productivity.

## Usage
### Pull (Download)
To download the latest version of ruby run,

```bash
docker pull ghcr.io/autamus/ruby:latest
```

or to download a specific version of ruby run,

```bash
docker pull ghcr.io/autamus/ruby:3.0.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/ruby ruby --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/ruby bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the ruby container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/ruby ruby /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC ruby container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-ruby/).
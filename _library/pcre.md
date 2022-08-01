---
layout: container
name: pcre
github: https://github.com/autamus/registry/blob/main/containers/p/pcre/spack.yaml
versions:
- "8.44"
- "8.45"
updated_at: 2022-08-01T19:25:56.860869478Z
size: 28MB
description: The PCRE package contains Perl Compatible Regular Expression libraries.
  These are useful for implementing regular expression pattern matching using the
  same syntax and semantics as Perl 5.
container_url: https://github.com/orgs/autamus/packages/container/package/pcre

---
# pcre
```bash 
Download        : docker pull ghcr.io/autamus/pcre
Compressed Size : 28MB
```

## Description
The PCRE package contains Perl Compatible Regular Expression libraries. These are useful for implementing regular expression pattern matching using the same syntax and semantics as Perl 5.

## Usage
### Pull (Download)
To download the latest version of pcre run,

```bash
docker pull ghcr.io/autamus/pcre:latest
```

or to download a specific version of pcre run,

```bash
docker pull ghcr.io/autamus/pcre:8.44
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/pcre pcre --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/pcre bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the pcre container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/pcre pcre /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC pcre container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-pcre/).
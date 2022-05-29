---
layout: container
name: swig
github: https://github.com/autamus/registry/blob/main/containers/s/swig/spack.yaml
versions:
- 4.0.2
updated_at: 2022-05-29T19:41:07.240632862Z
size: 29MB
description: SWIG is an interface compiler that connects programs written in C and
  C++ with scripting languages such as Perl, Python, Ruby, and Tcl. It works by taking
  the declarations found in C/C++ header files and using them to generate the wrapper
  code that scripting languages need to access the underlying C/C++ code. In addition,
  SWIG provides a variety of customization features that let you tailor the wrapping
  process to suit your application.
container_url: https://github.com/orgs/autamus/packages/container/package/swig

---
# swig
```bash 
Download        : docker pull ghcr.io/autamus/swig
Compressed Size : 29MB
```

## Description
SWIG is an interface compiler that connects programs written in C and C++ with scripting languages such as Perl, Python, Ruby, and Tcl. It works by taking the declarations found in C/C++ header files and using them to generate the wrapper code that scripting languages need to access the underlying C/C++ code. In addition, SWIG provides a variety of customization features that let you tailor the wrapping process to suit your application.

## Usage
### Pull (Download)
To download the latest version of swig run,

```bash
docker pull ghcr.io/autamus/swig:latest
```

or to download a specific version of swig run,

```bash
docker pull ghcr.io/autamus/swig:4.0.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/swig swig --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/swig bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the swig container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/swig swig /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC swig container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-swig/).
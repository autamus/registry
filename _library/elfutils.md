---
layout: container
name: elfutils
github: https://github.com/autamus/registry/blob/main/containers/e/elfutils/spack.yaml
versions:
- "0.185"
- "0.186"
- "0.187"
- "0.188"
updated_at: 2022-11-07T14:55:09.400705548Z
size: 43MB
description: elfutils is a collection of various binary tools such as eu-objdump,
  eu-readelf, and other utilities that allow you to inspect and manipulate ELF files.
  Refer to Table 5.Tools Included in elfutils for Red Hat Developer for a complete
  list of binary tools that are distributed with the Red Hat Developer Toolset version
  of elfutils.
container_url: https://github.com/orgs/autamus/packages/container/package/elfutils

---
# elfutils
```bash 
Download        : docker pull ghcr.io/autamus/elfutils
Compressed Size : 43MB
```

## Description
elfutils is a collection of various binary tools such as eu-objdump, eu-readelf, and other utilities that allow you to inspect and manipulate ELF files. Refer to Table 5.Tools Included in elfutils for Red Hat Developer for a complete list of binary tools that are distributed with the Red Hat Developer Toolset version of elfutils.

## Usage
### Pull (Download)
To download the latest version of elfutils run,

```bash
docker pull ghcr.io/autamus/elfutils:latest
```

or to download a specific version of elfutils run,

```bash
docker pull ghcr.io/autamus/elfutils:0.185
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/elfutils elfutils --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/elfutils bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the elfutils container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/elfutils elfutils /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC elfutils container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-elfutils/).
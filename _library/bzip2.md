---
layout: container
name: bzip2
github: https://github.com/autamus/registry/blob/main/containers/b/bzip2/spack.yaml
versions:
- 1.0.8
updated_at: 2022-08-01T18:08:02.801803586Z
size: 26MB
description: bzip2 is a freely available, patent free high-quality data compressor.
  It typically compresses files to within 10% to 15% of the best available techniques
  (the PPM family of statistical compressors), whilst being around twice as fast at
  compression and six times faster at decompression.
container_url: https://github.com/orgs/autamus/packages/container/package/bzip2

---
# bzip2
```bash 
Download        : docker pull ghcr.io/autamus/bzip2
Compressed Size : 26MB
```

## Description
bzip2 is a freely available, patent free high-quality data compressor. It typically compresses files to within 10% to 15% of the best available techniques (the PPM family of statistical compressors), whilst being around twice as fast at compression and six times faster at decompression.

## Usage
### Pull (Download)
To download the latest version of bzip2 run,

```bash
docker pull ghcr.io/autamus/bzip2:latest
```

or to download a specific version of bzip2 run,

```bash
docker pull ghcr.io/autamus/bzip2:1.0.8
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/bzip2 bzip2 --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/bzip2 bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the bzip2 container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/bzip2 bzip2 /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC bzip2 container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-bzip2/).
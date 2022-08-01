---
layout: container
name: ffmpeg
github: https://github.com/autamus/registry/blob/main/containers/f/ffmpeg/spack.yaml
versions:
- 4.3.2
- 4.4.1
- "4.5"
updated_at: 2022-08-01T18:31:04.451801596Z
size: 51MB
description: FFmpeg is a complete, cross-platform solution to record, convert and
  stream audio and video.
container_url: https://github.com/orgs/autamus/packages/container/package/ffmpeg

---
# ffmpeg
```bash 
Download        : docker pull ghcr.io/autamus/ffmpeg
Compressed Size : 51MB
```

## Description
FFmpeg is a complete, cross-platform solution to record, convert and stream audio and video.

## Usage
### Pull (Download)
To download the latest version of ffmpeg run,

```bash
docker pull ghcr.io/autamus/ffmpeg:latest
```

or to download a specific version of ffmpeg run,

```bash
docker pull ghcr.io/autamus/ffmpeg:4.3.2
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/ffmpeg ffmpeg --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/ffmpeg bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the ffmpeg container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/ffmpeg ffmpeg /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC ffmpeg container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-ffmpeg/).
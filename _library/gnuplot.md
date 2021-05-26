---
layout: container
name: gnuplot
github: https://github.com/autamus/registry/blob/main/containers/g/gnuplot/spack.yaml
versions:
- 5.2.8
updated_at: 2021-05-26T07:43:53.643320687Z
size: 174MB
description: 'Gnuplot is a portable command-line driven graphing utility for Linux,
  OS/2, MS Windows, OSX, VMS, and many other platforms. The source code is copyrighted
  but freely distributed (i.e., you don''t have to pay for it). It was originally
  created to allow scientists and students to visualize mathematical functions and
  data interactively, but has grown to support many non-interactive uses such as web
  scripting. It is also used as a plotting engine by third-party applications like
  Octave. Gnuplot has been supported and under active development since 1986 '
container_url: https://github.com/orgs/autamus/packages/container/package/gnuplot

---
# gnuplot
```bash 
Download        : docker pull ghcr.io/autamus/gnuplot
Compressed Size : 174MB
```

## Description
Gnuplot is a portable command-line driven graphing utility for Linux, OS/2, MS Windows, OSX, VMS, and many other platforms. The source code is copyrighted but freely distributed (i.e., you don't have to pay for it). It was originally created to allow scientists and students to visualize mathematical functions and data interactively, but has grown to support many non-interactive uses such as web scripting. It is also used as a plotting engine by third-party applications like Octave. Gnuplot has been supported and under active development since 1986 

## Usage
### Pull (Download)
To download the latest version of gnuplot run,

```bash
docker pull ghcr.io/autamus/gnuplot:latest
```

or to download a specific version of gnuplot run,

```bash
docker pull ghcr.io/autamus/gnuplot:5.2.8
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/gnuplot gnuplot --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/gnuplot bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the gnuplot container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/gnuplot gnuplot /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC gnuplot container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-gnuplot/).
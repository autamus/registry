---
layout: container
name:  "ghcr.io/autamus/ffmpeg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/ffmpeg/container.yaml"
updated_at: "2021-05-23 12:56:58.780736"
container_url: "https://github.com/orgs/autamus/packages/container/package/ffmpeg"
aliases:
 - "ffmpeg"

 - "ffprobe"

versions:
 - "4.5"
 - "latest"
description: "FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams."
---

This module is a singularity container wrapper for ghcr.io/autamus/ffmpeg.
FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/ffmpeg
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/ffmpeg:4.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/ffmpeg/4.5
$ module help ghcr.io/autamus/ffmpeg/4.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-ffmpeg-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-ffmpeg-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-ffmpeg-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-ffmpeg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-ffmpeg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ffmpeg
       
```bash
$ singularity exec <container> /opt/view/bin/ffmpeg
```


#### ffprobe
       
```bash
$ singularity exec <container> /opt/view/bin/ffprobe
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For each of the above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)

<br>
  
### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)
---
layout: container
name:  "ghcr.io/autamus/rclone"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/rclone/container.yaml"
updated_at: "2021-05-23 12:56:49.821496"
container_url: "https://github.com/orgs/autamus/packages/container/package/rclone"
aliases:
 - "rclone"

versions:
 - "1.55.0"
 - "1.55.1"
 - "latest"
description: "Rclone is a command line program to manage files on cloud storage."
---

This module is a singularity container wrapper for ghcr.io/autamus/rclone.
Rclone is a command line program to manage files on cloud storage.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/rclone
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/rclone:1.55.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/rclone/1.55.0
$ module help ghcr.io/autamus/rclone/1.55.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-rclone-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-rclone-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-rclone-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-rclone-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-rclone-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rclone
       
```bash
$ singularity exec <container> /opt/view/bin/rclone
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
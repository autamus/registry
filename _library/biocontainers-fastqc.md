---
layout: container
name:  "biocontainers/fastqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/fastqc/container.yaml"
updated_at: "2021-05-23 12:57:19.180070"
container_url: "https://hub.docker.com/r/biocontainers/fastqc"

versions:
 - "v0.11.5"
 - "v0.11.9_cv8"
description: "A quality control tool for high throughput sequence data."
---

This module is a singularity container wrapper for biocontainers/fastqc.
A quality control tool for high throughput sequence data.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install biocontainers/fastqc
```

Or a specific version:

```bash
$ shpc install biocontainers/fastqc:v0.11.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/fastqc/v0.11.5
$ module help biocontainers/fastqc/v0.11.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-fastqc-run:

```bash
$ singularity run <container>
```

#### biocontainers-fastqc-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-fastqc-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-fastqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-fastqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### biocontainers-fastqc

```bash
$ singularity run <container>
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
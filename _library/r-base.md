---
layout: container
name:  "r-base"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/r-base/container.yaml"
updated_at: "2021-05-23 12:57:23.100859"
container_url: "https://hub.docker.com/_/r-base"
aliases:
 - "R"

 - "Rscript"

versions:
 - "4.1.0"
 - "latest"
description: "R is a system for statistical computation and graphics."
---

This module is a singularity container wrapper for r-base.
R is a system for statistical computation and graphics.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install r-base
```

Or a specific version:

```bash
$ shpc install r-base:4.1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load r-base/4.1.0
$ module help r-base/4.1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### r-base-run:

```bash
$ singularity run <container>
```

#### r-base-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### r-base-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### r-base-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-base-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### R
       
```bash
$ singularity exec <container> /usr/bin/R
```


#### Rscript
       
```bash
$ singularity exec <container> /usr/bin/Rscript
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
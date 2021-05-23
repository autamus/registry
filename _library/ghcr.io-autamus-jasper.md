---
layout: container
name:  "ghcr.io/autamus/jasper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/jasper/container.yaml"
updated_at: "2021-05-23 12:56:58.129419"
container_url: "https://github.com/orgs/autamus/packages/container/package/jasper"
aliases:
 - "jasper"

 - "jpegtran"

versions:
 - "2.0.32"
 - "latest"
description: "JasPer is a collection of software (i.e., a library and application programs) for the coding and manipulation of images."
---

This module is a singularity container wrapper for ghcr.io/autamus/jasper.
JasPer is a collection of software (i.e., a library and application programs) for the coding and manipulation of images.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/jasper
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/jasper:2.0.32
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/jasper/2.0.32
$ module help ghcr.io/autamus/jasper/2.0.32
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-jasper-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-jasper-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-jasper-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-jasper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-jasper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jasper
       
```bash
$ singularity exec <container> /opt/view/bin/jasper
```


#### jpegtran
       
```bash
$ singularity exec <container> /opt/view/bin/jpegtran
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
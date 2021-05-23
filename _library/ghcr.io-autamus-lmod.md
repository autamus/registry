---
layout: container
name:  "ghcr.io/autamus/lmod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/lmod/container.yaml"
updated_at: "2021-05-23 12:56:45.392696"
container_url: "https://github.com/orgs/autamus/packages/container/package/lmod"
aliases:
 - "module"

versions:
 - "8.3"
 - "latest"
description: "The Persistence of Vision Ray Tracer, most commonly acronymed as POV-Ray, is a cross-platform ray-tracing program that generates images from a text-based scene description."
---

This module is a singularity container wrapper for ghcr.io/autamus/lmod.
The Persistence of Vision Ray Tracer, most commonly acronymed as POV-Ray, is a cross-platform ray-tracing program that generates images from a text-based scene description.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/lmod
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/lmod:8.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/lmod/8.3
$ module help ghcr.io/autamus/lmod/8.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-lmod-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-lmod-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-lmod-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-lmod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-lmod-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### module
       
```bash
$ singularity exec <container> . /opt/view/lmod/8.3/init/profile && module
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
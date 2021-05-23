---
layout: container
name:  "ghcr.io/autamus/ascent"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/ascent/container.yaml"
updated_at: "2021-05-23 12:56:52.227416"
container_url: "https://github.com/orgs/autamus/packages/container/package/ascent"

versions:
 - "0.7.0"
 - "0.7.1"
 - "latest"
description: "An open source many-core capable lightweight in situ visualization and analysis infrastructure for multi-physics HPC simulations."
---

This module is a singularity container wrapper for ghcr.io/autamus/ascent.
An open source many-core capable lightweight in situ visualization and analysis infrastructure for multi-physics HPC simulations.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/ascent
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/ascent:0.7.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/ascent/0.7.0
$ module help ghcr.io/autamus/ascent/0.7.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-ascent-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-ascent-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-ascent-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-ascent-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-ascent-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ghcr.io-autamus-ascent

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
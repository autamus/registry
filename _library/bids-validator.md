---
layout: container
name:  "bids/validator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/bids/validator/container.yaml"
updated_at: "2021-05-23 12:57:13.952404"
container_url: "https://hub.docker.com/r/bids/validator"
aliases:
 - "bids-validator"

versions:
 - "latest"
 - "v1.7.0"
 - "v1.7.1"
 - "v1.7.3-dev.0"
description: "A validator for BIDS (Brain Imaging Data Structure) datasets."
---

This module is a singularity container wrapper for bids/validator.
A validator for BIDS (Brain Imaging Data Structure) datasets.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install bids/validator
```

Or a specific version:

```bash
$ shpc install bids/validator:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/validator/latest
$ module help bids/validator/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### bids-validator-run:

```bash
$ singularity run <container>
```

#### bids-validator-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### bids-validator-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### bids-validator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bids-validator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bids-validator
       
```bash
$ singularity exec <container> /usr/local/bin/bids-validator
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
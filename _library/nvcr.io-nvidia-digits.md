---
layout: container
name:  "nvcr.io/nvidia/digits"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/nvidia/digits/container.yaml"
updated_at: "2021-05-23 12:57:16.639395"
container_url: "https://ngc.nvidia.com/catalog/containers/nvidia:digits/tags"
aliases:
 - "python"

versions:
 - "21.02-tensorflow-py3"
 - "21.03-tensorflow-py3"
 - "21.04-tensorflow-py3"
 - "21.05-tensorflow-py3"
description: "The NVIDIA Deep Learning GPU Training System (DIGITS) puts the power of deep learning into the hands of engineers and data scientists."
---

This module is a singularity container wrapper for nvcr.io/nvidia/digits.
The NVIDIA Deep Learning GPU Training System (DIGITS) puts the power of deep learning into the hands of engineers and data scientists.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install nvcr.io/nvidia/digits
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/digits:21.02-tensorflow-py3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/digits/21.02-tensorflow-py3
$ module help nvcr.io/nvidia/digits/21.02-tensorflow-py3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### nvcr.io-nvidia-digits-run:

```bash
$ singularity run <container>
```

#### nvcr.io-nvidia-digits-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### nvcr.io-nvidia-digits-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### nvcr.io-nvidia-digits-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nvcr.io-nvidia-digits-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python
       
```bash
$ singularity exec --nv <container> /usr/bin/python
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
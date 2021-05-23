---
layout: container
name:  "ghcr.io/autamus/python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/python/container.yaml"
updated_at: "2021-05-23 12:56:56.530015"
container_url: "https://github.com/orgs/autamus/packages/container/package/python"
aliases:
 - "pydoc3"

 - "pydoc3.8"

 - "python"

 - "python-config"

 - "python3"

 - "python3-config"

 - "python3.8"

 - "python3.8-config"

 - "python3.8-gdb.py"

versions:
 - "latest"
description: "An interpreted, high-level and general-purpose programming language."
---

This module is a singularity container wrapper for ghcr.io/autamus/python.
An interpreted, high-level and general-purpose programming language.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/python
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/python:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/python/latest
$ module help ghcr.io/autamus/python/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-python-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-python-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-python-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pydoc3
       
```bash
$ singularity exec <container> /opt/view/bin/pydoc3
```


#### pydoc3.8
       
```bash
$ singularity exec <container> /opt/view/bin/pydoc3.8
```


#### python
       
```bash
$ singularity exec <container> /opt/view/bin/python
```


#### python-config
       
```bash
$ singularity exec <container> /opt/view/bin/python-config
```


#### python3
       
```bash
$ singularity exec <container> /opt/view/bin/python3
```


#### python3-config
       
```bash
$ singularity exec <container> /opt/view/bin/python3-config
```


#### python3.8
       
```bash
$ singularity exec <container> /opt/view/bin/python3.8
```


#### python3.8-config
       
```bash
$ singularity exec <container> /opt/view/bin/python3.8-config
```


#### python3.8-gdb.py
       
```bash
$ singularity exec <container> /opt/view/bin/python3.8-gdb.py
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
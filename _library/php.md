---
layout: container
name:  "php"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/php/container.yaml"
updated_at: "2021-05-23 12:56:38.709014"
container_url: "https://hub.docker.com/_/php"
aliases:
 - "php"

 - "php-cgi"

 - "php-config"

 - "phpdbg"

 - "phpize"

versions:
 - "7.3.27-zts-alpine3.12"
 - "8.0.3-alpine"
 - "8.0.5-alpine"
 - "8.0.6-alpine"
 - "latest"
description: "While designed for web development, the PHP scripting language also provides general-purpose use."
---

This module is a singularity container wrapper for php.
While designed for web development, the PHP scripting language also provides general-purpose use.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install php
```

Or a specific version:

```bash
$ shpc install php:7.3.27-zts-alpine3.12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load php/7.3.27-zts-alpine3.12
$ module help php/7.3.27-zts-alpine3.12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### php-run:

```bash
$ singularity run <container>
```

#### php-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### php-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### php-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### php-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### php
       
```bash
$ singularity exec <container> /usr/local/bin/php
```


#### php-cgi
       
```bash
$ singularity exec <container> /usr/local/bin/php-cgi
```


#### php-config
       
```bash
$ singularity exec <container> /usr/local/bin/php-config
```


#### phpdbg
       
```bash
$ singularity exec <container> /usr/local/bin/phpdbg
```


#### phpize
       
```bash
$ singularity exec <container> /usr/local/bin/phpize
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
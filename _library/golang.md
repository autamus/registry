---
layout: container
name:  "golang"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/golang/container.yaml"
updated_at: "2021-05-23 12:57:18.476040"
container_url: "https://hub.docker.com/r/_/golang"
aliases:
 - "go"

 - "gofmt"

versions:
 - "1.16.4-alpine"
 - "latest"
description: "Go (a.k.a., Golang) is a programming language first developed at Google."
---

This module is a singularity container wrapper for golang.
Go (a.k.a., Golang) is a programming language first developed at Google.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install golang
```

Or a specific version:

```bash
$ shpc install golang:1.16.4-alpine
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load golang/1.16.4-alpine
$ module help golang/1.16.4-alpine
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### golang-run:

```bash
$ singularity run <container>
```

#### golang-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### golang-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### golang-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### golang-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### go
       
```bash
$ singularity exec <container> /usr/local/go/bin/go
```


#### gofmt
       
```bash
$ singularity exec <container> /usr/local/go/bin/gofmt
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
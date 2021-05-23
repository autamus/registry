---
layout: container
name:  "solr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/solr/container.yaml"
updated_at: "2021-05-23 12:57:25.100763"
container_url: "https://hub.docker.com/_/solr"
aliases:
 - "post"

 - "postlogs"

 - "solr"

versions:
 - "8.8.2-slim"
 - "latest"
description: "Solr is the popular, blazing-fast, open source enterprise search platform built on Apache Lucene™."
---

This module is a singularity container wrapper for solr.
Solr is the popular, blazing-fast, open source enterprise search platform built on Apache Lucene™.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install solr
```

Or a specific version:

```bash
$ shpc install solr:8.8.2-slim
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load solr/8.8.2-slim
$ module help solr/8.8.2-slim
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### solr-run:

```bash
$ singularity run <container>
```

#### solr-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### solr-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### solr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### solr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### post
       
```bash
$ singularity exec <container> /opt/solr/bin/post
```


#### postlogs
       
```bash
$ singularity exec <container> /opt/solr/bin/postlogs
```


#### solr
       
```bash
$ singularity exec <container> /opt/solr/bin/solr
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
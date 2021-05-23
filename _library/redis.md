---
layout: container
name:  "redis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/redis/container.yaml"
updated_at: "2021-05-23 12:57:25.975084"
container_url: "https://hub.docker.com/r/_/redis"
aliases:
 - "redis-benchmark"

 - "redis-check-aof"

 - "redis-check-rdb"

 - "redis-cli"

 - "redis-sentinel"

 - "redis-server"

versions:
 - "6.2.3-alpine"
 - "latest"
description: "Redis is an open-source, networked, in-memory, key-value data store with optional durability."
---

This module is a singularity container wrapper for redis.
Redis is an open-source, networked, in-memory, key-value data store with optional durability.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install redis
```

Or a specific version:

```bash
$ shpc install redis:6.2.3-alpine
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load redis/6.2.3-alpine
$ module help redis/6.2.3-alpine
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### redis-run:

```bash
$ singularity run <container>
```

#### redis-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### redis-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### redis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### redis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### redis-benchmark
       
```bash
$ singularity exec <container> /usr/local/bin/redis-benchmark
```


#### redis-check-aof
       
```bash
$ singularity exec <container> /usr/local/bin/redis-check-aof
```


#### redis-check-rdb
       
```bash
$ singularity exec <container> /usr/local/bin/redis-check-rdb
```


#### redis-cli
       
```bash
$ singularity exec <container> /usr/local/bin/redis-cli
```


#### redis-sentinel
       
```bash
$ singularity exec <container> /usr/local/bin/redis-sentinel
```


#### redis-server
       
```bash
$ singularity exec <container> /usr/local/bin/redis-server
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
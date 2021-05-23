---
layout: container
name:  "node"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/node/container.yaml"
updated_at: "2021-05-23 12:57:25.325236"
container_url: "https://hub.docker.com/r/_/node"
aliases:
 - "node"

 - "nodejs"

 - "npm"

 - "npx"

 - "yarn"

 - "yarnpkg"

versions:
 - "15.14.0-alpine"
 - "16.0.0-alpine"
 - "16.1.0-alpine"
 - "16.2.0-alpine"
 - "latest"
description: "Node.js is a software platform for scalable server-side and networking applications."
---

This module is a singularity container wrapper for node.
Node.js is a software platform for scalable server-side and networking applications.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install node
```

Or a specific version:

```bash
$ shpc install node:15.14.0-alpine
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load node/15.14.0-alpine
$ module help node/15.14.0-alpine
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### node-run:

```bash
$ singularity run <container>
```

#### node-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### node-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### node-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### node-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### node
       
```bash
$ singularity exec <container> /usr/local/bin/node
```


#### nodejs
       
```bash
$ singularity exec <container> /usr/local/bin/nodejs
```


#### npm
       
```bash
$ singularity exec <container> /usr/local/bin/npm
```


#### npx
       
```bash
$ singularity exec <container> /usr/local/bin/npx
```


#### yarn
       
```bash
$ singularity exec <container> /usr/local/bin/yarn
```


#### yarnpkg
       
```bash
$ singularity exec <container> /usr/local/bin/yarnpkg
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
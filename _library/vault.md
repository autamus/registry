---
layout: container
name:  "vault"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/vault/container.yaml"
updated_at: "2021-05-23 12:57:25.543537"
container_url: "https://hub.docker.com/_/vault"
aliases:
 - "vault"

versions:
 - "1.4.7"
 - "1.7.1"
 - "latest"
description: "Vault is a tool for securely accessing secrets via a unified interface and tight access control."
---

This module is a singularity container wrapper for vault.
Vault is a tool for securely accessing secrets via a unified interface and tight access control.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install vault
```

Or a specific version:

```bash
$ shpc install vault:1.4.7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load vault/1.4.7
$ module help vault/1.4.7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### vault-run:

```bash
$ singularity run <container>
```

#### vault-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### vault-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### vault-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vault-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vault
       
```bash
$ singularity exec <container> /bin/vault
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
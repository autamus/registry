---
layout: container
name:  "ghcr.io/autamus/mafft"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/mafft/container.yaml"
updated_at: "2021-05-23 12:56:58.566516"
container_url: "https://github.com/orgs/autamus/packages/container/package/mafft"
aliases:
 - "mafft"

 - "mafft-distance"

 - "mafft-einsi"

 - "mafft-fftns"

 - "mafft-fftnsi"

 - "mafft-ginsi"

 - "mafft-linsi"

 - "mafft-nwns"

 - "mafft-nwnsi"

 - "mafft-profile"

 - "mafft-qinsi"

 - "mafft-xinsi"

versions:
 - "7.475"
 - "latest"
description: "MAFFT is a multiple sequence alignment program for unix-like operating systems."
---

This module is a singularity container wrapper for ghcr.io/autamus/mafft.
MAFFT is a multiple sequence alignment program for unix-like operating systems.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/mafft
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/mafft:7.475
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/mafft/7.475
$ module help ghcr.io/autamus/mafft/7.475
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-mafft-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-mafft-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-mafft-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-mafft-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-mafft-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mafft
       
```bash
$ singularity exec <container> /opt/view/bin/mafft
```


#### mafft-distance
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-distance
```


#### mafft-einsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-einsi
```


#### mafft-fftns
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-fftns
```


#### mafft-fftnsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-fftnsi
```


#### mafft-ginsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-ginsi
```


#### mafft-linsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-linsi
```


#### mafft-nwns
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-nwns
```


#### mafft-nwnsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-nwnsi
```


#### mafft-profile
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-profile
```


#### mafft-qinsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-qinsi
```


#### mafft-xinsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-xinsi
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
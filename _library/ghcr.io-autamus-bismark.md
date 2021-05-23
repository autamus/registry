---
layout: container
name:  "ghcr.io/autamus/bismark"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/bismark/container.yaml"
updated_at: "2021-05-23 12:56:40.036482"
container_url: "https://github.com/orgs/autamus/packages/container/package/bismark"
aliases:
 - "bismark"

 - "bismark_genome_preparation"

 - "bismark_methylation_extractor"

 - "bismark2bedGraph"

 - "bismark2report"

 - "bismark2summary"

versions:
 - "0.23.0"
 - "latest"
description: "Bismark is a program to map bisulfite treated sequencing reads to a genome of interest and perform methylation calls in a single step."
---

This module is a singularity container wrapper for ghcr.io/autamus/bismark.
Bismark is a program to map bisulfite treated sequencing reads to a genome of interest and perform methylation calls in a single step.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/bismark
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/bismark:0.23.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/bismark/0.23.0
$ module help ghcr.io/autamus/bismark/0.23.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-bismark-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-bismark-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-bismark-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-bismark-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-bismark-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bismark
       
```bash
$ singularity exec <container> /opt/view/bin/bismark
```


#### bismark_genome_preparation
       
```bash
$ singularity exec <container> /opt/view/bin/bismark_genome_preparation
```


#### bismark_methylation_extractor
       
```bash
$ singularity exec <container> /opt/view/bin/bismark_methylation_extractor
```


#### bismark2bedGraph
       
```bash
$ singularity exec <container> /opt/view/bin/bismark2bedGraph
```


#### bismark2report
       
```bash
$ singularity exec <container> /opt/view/bin/bismark2report
```


#### bismark2summary
       
```bash
$ singularity exec <container> /opt/view/bin/bismark2summary
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
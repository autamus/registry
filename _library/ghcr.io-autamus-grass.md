---
layout: container
name:  "ghcr.io/autamus/grass"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/grass/container.yaml"
updated_at: "2021-05-23 12:56:46.058608"
container_url: "https://github.com/orgs/autamus/packages/container/package/grass"
aliases:
 - "grass78"

versions:
 - "7.8.5"
 - "latest"
description: "GRASS GIS (https://grass.osgeo.org/) is a Geographic Information System used for geospatial data management and analysis, image processing, graphics/map production, spatial modeling, and visualization."
---

This module is a singularity container wrapper for ghcr.io/autamus/grass.
GRASS GIS (https://grass.osgeo.org/) is a Geographic Information System used for geospatial data management and analysis, image processing, graphics/map production, spatial modeling, and visualization.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/grass
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/grass:7.8.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/grass/7.8.5
$ module help ghcr.io/autamus/grass/7.8.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-grass-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-grass-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-grass-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-grass-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-grass-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grass78
       
```bash
$ singularity exec <container> /opt/view/bin/grass78
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
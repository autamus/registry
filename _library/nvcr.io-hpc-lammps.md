---
layout: container
name:  "nvcr.io/hpc/lammps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/hpc/lammps/container.yaml"
updated_at: "2021-05-23 12:57:18.030804"
container_url: "https://ngc.nvidia.com/catalog/containers/hpc:lammps/tags"

versions:
 - "29Oct2020"
description: "Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) is a software application designed for molecular dynamics simulations. It has the potentials for solid-state materials (metals, semiconductor), soft matter (biomolecules, polymers), and coarse-grained or mesoscopic systems. The main use-case is atom scale particle modeling or, more generically, as a parallel particle simulator at the atomic, meson, or continuum scale. LAMMPS runs on single processors or in parallel using message-passing techniques and a spatial-decomposition of the simulation domain. Read more on the LAMMPS website https://lammps.sandia.gov/."
---

This module is a singularity container wrapper for nvcr.io/hpc/lammps.
Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) is a software application designed for molecular dynamics simulations. It has the potentials for solid-state materials (metals, semiconductor), soft matter (biomolecules, polymers), and coarse-grained or mesoscopic systems. The main use-case is atom scale particle modeling or, more generically, as a parallel particle simulator at the atomic, meson, or continuum scale. LAMMPS runs on single processors or in parallel using message-passing techniques and a spatial-decomposition of the simulation domain. Read more on the LAMMPS website https://lammps.sandia.gov/.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install nvcr.io/hpc/lammps
```

Or a specific version:

```bash
$ shpc install nvcr.io/hpc/lammps:29Oct2020
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/hpc/lammps/29Oct2020
$ module help nvcr.io/hpc/lammps/29Oct2020
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### nvcr.io-hpc-lammps-run:

```bash
$ singularity run <container>
```

#### nvcr.io-hpc-lammps-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### nvcr.io-hpc-lammps-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### nvcr.io-hpc-lammps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nvcr.io-hpc-lammps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### nvcr.io-hpc-lammps

```bash
$ singularity run <container>
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
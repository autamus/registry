---
layout: container
name:  "ruby"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ruby/container.yaml"
updated_at: "2021-05-23 12:57:18.708170"
container_url: "https://hub.docker.com/_/ruby"
aliases:
 - "bundle"

 - "bundler"

 - "erb"

 - "gem"

 - "irb"

 - "racc"

 - "rake"

 - "rbs"

 - "rdoc"

 - "ri"

 - "ruby"

 - "typeprof"

versions:
 - "3.0.1-alpine"
 - "latest"
description: "Ruby is a dynamic, reflective, object-oriented, general-purpose, open-source programming language."
---

This module is a singularity container wrapper for ruby.
Ruby is a dynamic, reflective, object-oriented, general-purpose, open-source programming language.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ruby
```

Or a specific version:

```bash
$ shpc install ruby:3.0.1-alpine
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ruby/3.0.1-alpine
$ module help ruby/3.0.1-alpine
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ruby-run:

```bash
$ singularity run <container>
```

#### ruby-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ruby-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ruby-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ruby-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bundle
       
```bash
$ singularity exec <container> /usr/local/bin/bundle
```


#### bundler
       
```bash
$ singularity exec <container> /usr/local/bin/bundler
```


#### erb
       
```bash
$ singularity exec <container> /usr/local/bin/erb
```


#### gem
       
```bash
$ singularity exec <container> /usr/local/bin/gem
```


#### irb
       
```bash
$ singularity exec <container> /usr/local/bin/irb
```


#### racc
       
```bash
$ singularity exec <container> /usr/local/bin/racc
```


#### rake
       
```bash
$ singularity exec <container> /usr/local/bin/rake
```


#### rbs
       
```bash
$ singularity exec <container> /usr/local/bin/rbs
```


#### rdoc
       
```bash
$ singularity exec <container> /usr/local/bin/rdoc
```


#### ri
       
```bash
$ singularity exec <container> /usr/local/bin/ri
```


#### ruby
       
```bash
$ singularity exec <container> /usr/local/bin/ruby
```


#### typeprof
       
```bash
$ singularity exec <container> /usr/local/bin/typeprof
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
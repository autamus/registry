---
layout: container
name:  "mysql"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/mysql/container.yaml"
updated_at: "2021-05-23 12:56:38.490388"
container_url: "https://hub.docker.com/r/_/mysql"
aliases:
 - "mysql"

 - "mysql_config_editor"

 - "mysql_secure_installation"

 - "mysql_ssl_rsa_setup"

 - "mysql_tzinfo_to_sql"

 - "mysql_upgrade"

 - "mysqladmin"

 - "mysqlbinlog"

 - "mysqlcheck"

 - "mysqld_multi"

 - "mysqld_safe"

 - "mysqldump"

 - "mysqldumpslow"

 - "mysqlimport"

 - "mysqlpump"

 - "mysqlshow"

 - "mysqlslap"

versions:
 - "8.0.25"
 - "latest"
description: "MySQL is the world's most popular open source database."
---

This module is a singularity container wrapper for mysql.
MySQL is the world's most popular open source database.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install mysql
```

Or a specific version:

```bash
$ shpc install mysql:8.0.25
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load mysql/8.0.25
$ module help mysql/8.0.25
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### mysql-run:

```bash
$ singularity run <container>
```

#### mysql-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### mysql-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### mysql-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mysql-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mysql
       
```bash
$ singularity exec <container> /usr/bin/mysql
```


#### mysql_config_editor
       
```bash
$ singularity exec <container> /usr/bin/mysql_config_editor
```


#### mysql_secure_installation
       
```bash
$ singularity exec <container> /usr/bin/mysql_secure_installation
```


#### mysql_ssl_rsa_setup
       
```bash
$ singularity exec <container> /usr/bin/mysql_ssl_rsa_setup
```


#### mysql_tzinfo_to_sql
       
```bash
$ singularity exec <container> /usr/bin/mysql_tzinfo_to_sql
```


#### mysql_upgrade
       
```bash
$ singularity exec <container> /usr/bin/mysql_upgrade
```


#### mysqladmin
       
```bash
$ singularity exec <container> /usr/bin/mysqladmin
```


#### mysqlbinlog
       
```bash
$ singularity exec <container> /usr/bin/mysqlbinlog
```


#### mysqlcheck
       
```bash
$ singularity exec <container> /usr/bin/mysqlcheck
```


#### mysqld_multi
       
```bash
$ singularity exec <container> /usr/bin/mysqld_multi
```


#### mysqld_safe
       
```bash
$ singularity exec <container> /usr/bin/mysqld_safe
```


#### mysqldump
       
```bash
$ singularity exec <container> /usr/bin/mysqldump
```


#### mysqldumpslow
       
```bash
$ singularity exec <container> /usr/bin/mysqldumpslow
```


#### mysqlimport
       
```bash
$ singularity exec <container> /usr/bin/mysqlimport
```


#### mysqlpump
       
```bash
$ singularity exec <container> /usr/bin/mysqlpump
```


#### mysqlshow
       
```bash
$ singularity exec <container> /usr/bin/mysqlshow
```


#### mysqlslap
       
```bash
$ singularity exec <container> /usr/bin/mysqlslap
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
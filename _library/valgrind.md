---
layout: container
name: valgrind
github: https://github.com/autamus/registry/blob/main/containers/v/valgrind/spack.yaml
versions:
- 3.17.0
updated_at: 2021-05-26T08:22:47.937447701Z
size: 97MB
description: ') depends_on(''mpi'', when=''+mpi'') depends_on(''boost'', when=''+boost'')
  depends_on("autoconf", type=''build'', when=''@develop'') depends_on("automake",
  type=''build'', when=''@develop'') depends_on("libtool", type=''build'', when=''@develop'')
  # Apply the patch suggested here: # http://valgrind.10908.n7.nabble.com/Unable-to-compile-on-Mac-OS-X-10-11-td57237.html
  patch(''valgrind_3_12_0_osx.patch'', when=''@3.12.0 platform=darwin'
container_url: https://github.com/orgs/autamus/packages/container/package/valgrind

---
# valgrind
```bash 
Download        : docker pull ghcr.io/autamus/valgrind
Compressed Size : 97MB
```

## Description
) depends_on('mpi', when='+mpi') depends_on('boost', when='+boost') depends_on("autoconf", type='build', when='@develop') depends_on("automake", type='build', when='@develop') depends_on("libtool", type='build', when='@develop') # Apply the patch suggested here: # http://valgrind.10908.n7.nabble.com/Unable-to-compile-on-Mac-OS-X-10-11-td57237.html patch('valgrind_3_12_0_osx.patch', when='@3.12.0 platform=darwin

## Usage
### Pull (Download)
To download the latest version of valgrind run,

```bash
docker pull ghcr.io/autamus/valgrind:latest
```

or to download a specific version of valgrind run,

```bash
docker pull ghcr.io/autamus/valgrind:3.17.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/valgrind valgrind --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/valgrind bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the valgrind container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/valgrind valgrind /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC valgrind container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-valgrind/).
---
layout: container
name: node-js
github: https://github.com/autamus/registry/blob/main/containers/n/node-js/spack.yaml
versions:
- 15.3.0
updated_at: 2021-11-17T16:05:58.749921751Z
size: 56MB
description: Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.
container_url: https://github.com/orgs/autamus/packages/container/package/node-js

---
# node-js
```bash 
Download        : docker pull ghcr.io/autamus/node-js
Compressed Size : 56MB
```

## Description
Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.

## Usage
### Pull (Download)
To download the latest version of node-js run,

```bash
docker pull ghcr.io/autamus/node-js:latest
```

or to download a specific version of node-js run,

```bash
docker pull ghcr.io/autamus/node-js:15.3.0
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/node-js node-js --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/node-js bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the node-js container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/node-js node-js /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluster. Check out the SHPC node-js container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-node-js/).
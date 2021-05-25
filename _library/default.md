# {{.Name}}
```bash 
Download        : docker pull ghcr.io/autamus/{{toHypen .Name}}
Compressed Size : {{.Size}}
```

## Description
{{.Description}}

## Usage
### Pull (Download)
To download the latest version of {{.Name}} run,

```bash
docker pull ghcr.io/autamus/{{toHypen .Name}}:latest
```

or to download a specific version of {{.Name}} run,

```bash
docker pull ghcr.io/autamus/{{toHypen .Name}}:{{index .Versions 0}}
```
### Run
To run the container as an application run,
```bash
docker run --rm ghcr.io/autamus/{{toHypen .Name}} {{toHypen .Name}} --version
```

or to run the container in an interactive session run,
```bash
docker run -it --rm ghcr.io/autamus/{{toHypen .Name}} bash
```

### Mounting volumes between the container and your machine
To access files from your machine within the {{.Name}} container you'll have to mount them using the `-v external/path:internal/path` option.

For example,
```bash
docker run -v ~/Documents/Data:/Data ghcr.io/autamus/{{toHypen .Name}} {{toHypen .Name}} /Data/myData.csv
```
which will mount the `~/Documents/Data` directory on your computer to the `/Data` directory within the container.

## HPC
If you're looking to use this container in an HPC environment we recommend using [Singularity-HPC](https://singularity-hpc.readthedocs.io) to use the container just as any other module on the cluser. Check out the SHPC {{.Name}} container [here](https://singularityhub.github.io/singularity-hpc/r/ghcr.io-autamus-{{toHypen .Name}}/).
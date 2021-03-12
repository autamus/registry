# Registry
<img src="https://avatars.githubusercontent.com/u/73002963" width="300" height="300">
The Core Registry of Container Blueprints for the Autamus Build System

## Table of Contents
- [Backstory](#backstory)
- [Introduction](#introduction)
- [Usage](#usage)
  - [Downloading A Container](#downloading-a-container)
  - [Submitting A Package](#submitting-a-package)

## Backstory
At the end of my undergraduate freshman year, as my internship with the University's Research & HPC Computing group was finishing up, a freind (@bjoyce3) and I (@alecbcs) were talking about the software installed on our University's local HPC. In particular, how the age of many of the analysis packages (and their depedencies) were keeping us from updating the operating systems of the clusters. During that conversation, we started dreaming about "an autonoumous build system" for scientific containers. One that would update containers as new versions of their source code became available, rebuild containers as a package's depedencies recieved updates, and thoroughly test the containers before publishing them. During that following summer, I was hired on by the HPC Team and this idea became a multi-year project. Although we've still got a ways to go handling depdencies and testing contaiers we're ready to begin building analysis packages for researchers. If this interests you as a researcher, research engineer, or system admin check below to see how you can submit packages and pull the built containers.

## Introduction
Autamus is an semi-autonomous build system for scientific containers. What do I mean by "semi-autonomous"? Well given that the source code of a package is hosted on GitHub, GitLab, Sourceforge, etc... our bot Binoc can tell when new versions of a package have been released and will submit those updates as Pull Requests to this repository and attempt to build the updated packages. Don't worry a human will always be in the loop to check over and approve an update for security. With Binoc's help however, container maintainers no longer have to spend their time remembering to check every package for updates. From the perspective of a user this also means you can spend less time submitting update requests and more time using whichever version of a container that you'd like.

## Usage
### Downloading A Container
Right now all of our packages are hosted on the GitHub Container Registry.

[Check Them Out Here!](https://github.com/orgs/autamus/packages)

### Submitting a Package
*note: At the moment we are only building single package containers although multi-package containers are coming soon!

1) Fork this repository (button at the top right of this page!)
2) Check out the [Spack Repository](https://spack.readthedocs.io/en/latest/package_list.html) to see if they have the package build instructions you are looking for. Or checkout the [Spack Docs](https://spack.readthedocs.io/en/latest/packaging_guide.html) to learn how to build your very of instruction file (called a Speck).
3) Add that package.py file (and any other nessiary files like patches) to a directory in your fork of this repository under `FIRST-LETTER-OF-APPLICATION/NAME-OF-APPLICATION/package.py`.
4) Commit that new directory to your fork and open a pull request on this repository from your fork.


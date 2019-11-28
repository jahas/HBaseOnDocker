# HBaseOnDocker
## Tested on:
* Linux (ok)
* Windows (not compatible)
* MacOS (not checked)

## Structure of a structure
```
.
├── environment.yml
├── initialize.sh
├── run-cloudera-docker.sh
├── setup.hbase
└── src

```

## Prerequisites

In order to use this code you should install:
* Conda (Miniconda is preferred since it is smaller and faster to install)
* Docker

## Preparations

Before you will run the docker image first you have to:
* Run `conda env create -f ./environment.yml -p ./conda/envs/hbase-env`

## Running the docker

### Setting up the container
To run the docker image it is enough to:
* Run command `sh ./run-cloudera-docker.sh`. It will start the container and return it's ID
* Run command `docker attach {docker container ID}`. It will startup the quickstart.cloudera.
* Inside docker run command `cd && sh ./initialize.sh`. It will add your conda env python to the path


### Playing with the container
**All commands from this section should be run inside the container from ~ location**
To setup new HBase table do this step:
* Inside docker run command `hbase shell ./setup.hbase`. It will add a table and fill it with some records.

In order to read the data from the table run this command: `python3.7 src/hbase-reader.py`

### Detach from container

To detach from the container without killing it use sequence `CTRL+P` and `CTRL+Q`

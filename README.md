Demo services that communicate with each other using kafka

# Installation

1. Ensure docker and docker-compose are installed

## Start all services

Run `docker-compose up -d`

* Zookeeper and kafka start and will take some time to initialize.
* When they are ready, init-kafka will create topics and exit.
* The python containers will start connecting to kafka after 20 seconds.

## Stop all services

`docker-compose down`

Optionally, to clean up all volumes,

`docker volume prune`

# The Cats, Dogs and their Owners API

## What this does:

This is the API supporting the [Optibrium Technical Test](https://github.com/optibrium/web_developer_tech_test), a specification for this API can be found [here](https://github.com/optibrium/web_developer_tech_test/blob/master/CDOAPI.md) 

## Requirements

This project only requires that Docker-Compose or Docker Swarm be installed

## Running the project locally

You can run this project with
```
docker-compose up
```
This will automatically Test, Lint and Build the project from local code. Note; if you edit the code you will have to supply the rebuild flag
```
docker-compose up --build
```
The server will then attempt bind and become available on port 8080

## Deploying the project

To deploy the API outside of a Docker Stack you simply require an environment variable `DATABASE` containing the [DSN](https://en.wikipedia.org/wiki/Data_source_name) of the database supporting the application. (An example DSN can be found in the docker-compose.yml file).  
Note that the application does NOT create its own database schema via migration, an example schema for PostgreSQL can be found in the postgres folder.

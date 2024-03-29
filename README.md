# cowry-service

A simple microservices books management system developed using FastAPI, postgres and Docker

- To acommplish a fully managed [microservices architecture](https://en.wikipedia.org/wiki/Microservices) setup, the books service (with it's own database) is created seperately as opposed to using a shared books database between the client and the admin.

- The services are routed to the same ports using [Nginx](https://www.nginx.com/) which in this case serves as both a reverse-proxy and api gateway
- the services communicate to each other via http using the [requests](https://docs.python-requests.org/en/latest/) library (you might want to consider using a more robust approach (events/message-brokers) like Redis, RabbitMQ, Kafka e.t.c)

### Build the initial docker images for your services

In the root of your project, run the command

```bash
 docker-compose up -d
```

### Running the Dev Docker container

To start the container of each service, use the following command:

```bash
 docker-compose up
```

## Please find the links to the docker images for each of the services below:

- [Books-Service](https://hub.docker.com/repository/docker/ewave112/cowry-service-books)
- [Client-Service](https://hub.docker.com/repository/docker/ewave112/cowry-service-user)
- [Admin-Service](https://hub.docker.com/repository/docker/ewave112/cowry-service-admin-api)

## Running Tests

- This project uses [pytest](https://docs.pytest.org/en/7.0.x/) for running tests
- You can test out each services (e.g client) by running the commands

```bash
 cd <service_name>
```

then run the test

```bash
 pytest
```

NB: It is assumed that the seeded data is actually in the database server of each service

## Foot notes

- It is not recommended to use alpine based images for this project(or most of other python projects) and here's [why](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker#-alpine-python-warning)

- A useful resource on how to push your docker image to [DockerHub](https://hub.docker.com) can be found [here](https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html)

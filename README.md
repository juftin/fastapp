# ml-server

## Directory Structure

```text
├── ml_server                   Docker Container Source Code
│   ├── app.py                  FastAPI App Configuration
│   ├── nginx.conf              Nginx Configuration File
│   └── serve.py                API Serving Script
├── Dockerfile                  Dockerfile for Project
├── requirements.txt            Project Dependencies
├── docker_entrypoint.sh        Docker Entrypoint file
├── VERSION                     Project Version (and Docker image tag)
├── README.md                   This documentation file :)
```

## Local Usage

### Building the Docker Image Locally

```shell
docker build \
    --tag juftin/ml-server:latest \
    .
```

### Serving the Model Locally

```shell
docker run --rm -it \
    --publish 8080:8080 \
    --volume ${PWD}/ml_server:/root/ml_server \
    juftin/ml-server:latest \
    serve-debug
```

### Testing Locally

#### Health Check

```shell
curl \
  --request GET \
  --silent \
  --header "Content-Type: application/json" \
  http://localhost:8080/ping \
  | jq
```

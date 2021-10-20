# flask-template
Get a Flask app skeleton at the moment

[![Docker Hub](https://img.shields.io/static/v1.svg?color=4edafc&labelColor=555555&logoColor=ffffff&style=flat&label=lcaparros/<appName>&message=Docker%20Hub&logo=docker)](https://hub.docker.com/r/lcaparros/<appName>)
[![Docker Pulls](https://img.shields.io/docker/pulls/lcaparros/<appName>.svg?color=4edafc&labelColor=555555&logoColor=ffffff&style=flat&label=pulls&logo=docker)](https://hub.docker.com/r/lcaparros/<appName>)
[![Docker Stars](https://img.shields.io/docker/stars/lcaparros/<appName>.svg?color=4edafc&labelColor=555555&logoColor=ffffff&style=flat&label=stars&logo=docker)](https://hub.docker.com/r/lcaparros/<appName>)
[![GitHub Repository](https://img.shields.io/static/v1.svg?color=4edafc&labelColor=555555&logoColor=ffffff&style=flat&label=lcaparros/docker-<appName>&message=GitHub%20Repo&logo=github)](https://github.com/lcaparros/docker-<appName>)
[![GitHub Stars](https://img.shields.io/github/stars/lcaparros/docker-<appName>.svg?color=4edafc&labelColor=555555&logoColor=ffffff&style=flat&logo=github)](https://github.com/lcaparros/docker-<appName>)
[![GitHub Release](https://img.shields.io/github/release/lcaparros/docker-<appName>.svg?color=4edafc&labelColor=555555&logoColor=ffffff&style=flat&logo=github)](https://github.com/lcaparros/docker-<appName>/releases)
[![GitHub](https://img.shields.io/static/v1.svg?color=4edafc&labelColor=555555&logoColor=ffffff&style=flat&label=lcaparros&message=GitHub&logo=github)](https://github.com/lcaparros "view the source for all of our repositories.")


## Development

To run locally the application export the next two environment variables>

```shell
export FLASK_APP=app/app
export FLASK_ENV=development
```

Then run the Flask server typing:

```shell
flask run
```

## Production

The recommended solution for production environment is to build the provided Dockerfile and run the application in a docker container. It can be done with:

```shell
docker build . -t flask_image
docker run --name flask_container -p 80:80 -v /logs:/srv/flask_app/logs flask_image
```

This dockerized version is using nginx to expose the service and uWSGI to serve.
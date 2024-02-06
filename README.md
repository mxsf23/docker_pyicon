# Docker + Python app test

## Description

Py scripts simply fetches favicon file from given url.

``````
get_favico.py -u URL
``````
## Dockerize it

Dockerfile - simple file for building docker image of this app.
Dockerfile2 - multistage variant of docker image.

Final images have almost the same size. 

Run:

``````
docker run --name test01 -v /tmp/icons:/tmp/icons <IMAGE>
``````
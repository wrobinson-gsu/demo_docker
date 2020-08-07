DOCKER RUN

WITHOUT A VOLUME

It's simpler to run without a mounted volumne (e.g., on GCP).

command line:
    docker build -t pmmlserver:1.0 .
    docker run -p:5000:5000 -d pmmlserver:1.0

WITH A VOLUME

In case of debugging code, you may want to have the Docker container use files from a local file system. Then, when you edit the files the container will automatially use the new code to update the web site. (Note: this takes longer, 1 minute, to start. Check the logs to see that it's done.)

command line:
    docker build -f DockerfileWithVolume -t pmmlserver:1.0 .
Linux shell or PowerShell
    docker run -v `pwd`:/app -p:5000:5000 -d pmmlserver:1.0
Windows Command shell
    docker run -v %cd%:/app -p:5000:5000 -d pmmlserver:1.0


MANUAL RUN

You can run using a larger (Python 3) image and then immediately open the (bash) shell to manually create and run the application in the (Python 3) container.

command line:
Linux shell or PowerShell
    docker run -v `pwd`:/app --rm -ti -p 5000:5000 python:3 bash
Windows Command shell
    docker run -v %cd%:/app --rm -ti -p 5000:5000 python:3 bash

In the running docker, run the following:
    pip install pypmml flask
    apt-get update
    apt-get install default-jdk
    cd /app
    python app.py


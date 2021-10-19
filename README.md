This repo is a example multi-tiered application that runs as a set of Docker containers.  The application is built using nginx as a reverse proxy to handle client requests, two Python based Flask apps to process requests, and a MongoDB database for persistence.  As illustrated below, each component runs as its own Docker container.

Instructions for building these images from included Dockerfiles are below.

<pre>
                                  +---------+
                             +--> |  app1   |
             +---------+    /     +---------+     +---------+
(Client) --> |  nginx  | --+----> |  app2   | --> | MongoDB |
             +---------+          +---------+     +---------+
</pre>


Working from right to left...

## Clone the repo and run below commands to run container:
```
docker run -d --name mongo mongo
docker build -t prajith/flask-uwsgi flask-uwsgi

docker build -t prajith/app1 app1
docker build -t prajith/app2 app2
docker run -d -P --name app1 prajith/app1
docker run -d -P --name app2 prajith/app2

docker build -t prajith/nginx nginx
docker run -d -p 80:80 --name nginx --link app1:app1 --volumes-from app1:ro --link app2:app2 --volumes-from app2:ro prajith/nginx
```

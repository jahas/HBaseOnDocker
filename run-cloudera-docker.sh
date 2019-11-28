#!/bin/bash
sudo docker run \
	--hostname=quickstart.cloudera \
	--privileged=true \
	-i -t \
	-p 8888:8888 \
	-d \
	-v `pwd`:/root/ \
	cloudera/quickstart \
	/usr/bin/docker-quickstart

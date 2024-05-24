#!/usr/bin/env bash
# A script that sets up my web servers for the deployment of "web_static"

nginx_config="events {}\n\nhttp {\n\tserver {\n\t\tlisten 80;\n\t\tlisten [::]:80;\n\n\t\tserver_name ahmad-basheer.tech;\n\n\t\tlocation /hbnb_static {\n\t\t\talias /data/web_static/current;\n\t\t}\n\t}\n}"

# Installing Nginx
apt-get -y install nginx

# Creating main "web_static" in the file system
mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "Configuration test: Success!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data

# Configuring Nginx to serve content of "/data/web_static/current" to
# http://ahmad-basheer.tech/hbnb_static
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
echo -e "$nginx_config" > /etc/nginx/nginx.conf
nginx -s reload

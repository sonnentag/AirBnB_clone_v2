#!/usr/bin/env bash
# sets up web servers for deployment of web_static

apt update
apt -y install nginx

mkdir -p /data/web_static/releases/test /data/web_static/shared

echo -e '<html>\n<head>\n</head>\n<body bgcolor=black>\nHolberton School\n</body>\n</html>' > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

sed -i '/^server/,/^}/s~^}~\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n}~' /etc/nginx/sites-available/default

service nginx restart

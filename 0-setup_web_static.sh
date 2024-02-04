#!/usr/bin/env bash
# sets up web servers for deployment of web_static

# install nginx if not installed
sudo apt update && sudo apt install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# echo files
echo "Test content" | sudo tee /data/web_static/releases/test/index.html > /dev/null
echo "Hello World!" | sudo tee /var/www/html/index.html > /dev/null

# create symbolic link
rm -rf /data/web_static/current && sudo ln -s /data/web_static/releases/"test" /data/web_static/current

# change ownership to ubuntu user & group
sudo chown -R ubuntu:ubuntu /data/

# update nginx to server static content tbc (use alias)

updated_config=$(cat <<eof

server {
	listen 80;

	root /var/www/html;
	server_name www.sao-rct.tech;

	add_header X-Served-By \$hostname;

	location = /redirect_me {
	return 301;
	}

	location / {

	try_files \$uri \$uri/ =404;
	}

	location /hbnb_static {
	alias /data/web_static/current/;
	}
}
eof
)

echo "$updated_config" | sudo tee /etc/nginx/sites-enabled/default >/dev/null

sudo nginx -qt && sudo service nginx start


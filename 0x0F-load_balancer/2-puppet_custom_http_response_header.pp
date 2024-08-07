#!/usr/bin/env bash
#This is a custom header using puppet

exec { 'http header':
	command => 'sudo apt-get update -y'
	sudo apt-get install nginx -y;
	sudo sed -i "/server_name _/a add_header X-Served-By HostName;" /etc/nginx/sites-available/default
	sudo service nginx restart',
	provider => shell,
}

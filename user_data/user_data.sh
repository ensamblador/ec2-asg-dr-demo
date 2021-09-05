#!/bin/bash
sudo su
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
echo "<html><h1> Hola desde aws girls perú! soy el servidor $(hostname -i) </h1><html>" >> /var/www/html/index.html
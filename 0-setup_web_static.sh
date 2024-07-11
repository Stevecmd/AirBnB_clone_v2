#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static.

################################################################################
# Script: setup_web_servers.sh
#
# Description:
# This script sets up web servers for the deployment of web_static.
# It installs Nginx if it is not already installed, creates necessary directories,
# generates a fake HTML file for testing, creates a symbolic link to the current
# release, sets ownership of directories, and updates Nginx configuration to serve
# web_static content.
#
# Usage:
# Run this script with sudo privileges on an Ubuntu server to configure it for
# serving web_static content with Nginx.
#
# Author: SteveCMD
# Date: 2024
#
################################################################################

# Function to install Nginx if it is not already installed
install_nginx() {
    if ! dpkg -l | grep -q nginx; then
        sudo apt-get update
        sudo apt-get install -y nginx
    fi
}

# Function to create directories if they do not already exist
create_directories() {
    sudo mkdir -p /data/web_static/releases/test/
    sudo mkdir -p /data/web_static/shared/
}

# Function to create a fake HTML file
create_fake_html() {
    echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
}

# Function to create a symbolic link
create_symbolic_link() {
    sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
}

# Function to set ownership of the /data/ folder
set_ownership() {
    sudo chown -R ubuntu:ubuntu /data/
}

# Function to update Nginx configuration
update_nginx_config() {
    # Check if the alias already exists in the Nginx configuration
    if ! grep -q "location /hbnb_static" /etc/nginx/sites-available/default; then
        sudo sed -i '/server_name _;/a \ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
        sudo systemctl restart nginx
    fi
}

# Main script execution
install_nginx
create_directories
create_fake_html
create_symbolic_link
set_ownership
update_nginx_config

echo "Web server setup for web_static deployment completed."

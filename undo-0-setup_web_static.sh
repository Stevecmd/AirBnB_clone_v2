#!/bin/bash

# Function to remove Nginx if it was installed by the script
remove_nginx() {
    if dpkg -l | grep -q nginx; then
        sudo apt-get remove --purge -y nginx nginx-common
        sudo apt-get autoremove -y
    fi
}

# Function to remove the directories created by the script
remove_directories() {
    sudo rm -rf /data/web_static/releases/test/
    sudo rm -rf /data/web_static/shared/
}

# Function to remove the fake HTML file created by the script
remove_fake_html() {
    sudo rm -f /data/web_static/releases/test/index.html
}

# Execute the undo functions
remove_nginx
remove_directories
remove_fake_html

echo "Undo of web server setup for web_static deployment completed."

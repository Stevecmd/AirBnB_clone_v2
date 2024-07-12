#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from datetime import datetime
from os.path import exists
from fabric.api import put, run, env, local
import os

env.hosts = ['54.160.94.43', '34.203.38.175']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_ed25519"
env.timeout = 60  # Increase timeout to 60 seconds


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The archive path if the archive has been correctly generated.
        None: If the archive was not generated.
    """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.

    Args:
        archive_path (str): Local path to the archive to be deployed.

    Returns:
        bool: True if deployment was successful, False otherwise.
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, no_ext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('sudo rm /tmp/{}'.format(file_n))
        run('sudo rsync -a {0}{1}/web_static/ {0}{1}/'.format(path, no_ext))
        run('sudo rm -rf {}{}/web_static'.format(path, no_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        # Update Nginx configuration to point to the new deployment directory
        nginx_config = """
        server {
            listen 80;
            server_name _;

            location / {
                alias /data/web_static/current/;
                index 0-index.html;
            }
        }
        """
        run(
            "echo '{}' | sudo tee /etc/nginx/sites-available/default"
            .format(nginx_config)
        )

        # Enable the new configuration by creating a symbolic link
        run(
            "sudo ln -sf /etc/nginx/sites-available/default "
            "/etc/nginx/sites-enabled/"
        )

        # Reload Nginx to apply the new configuration
        run("sudo service nginx reload")

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error deploying: {str(e)}")
        return False

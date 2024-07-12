#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.160.94.43', '34.203.38.175']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_ed25519"


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The archive path if the archive has been correctly generated.
        None: If the archive was not generated.
    """
    local("mkdir -p versions")
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
    if not os.path.exists(archive_path):
        print(f"Error: Archive '{archive_path}' not found.")
        return False

    try:
        # Extract file name from path
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file

        # Upload archive to /tmp/ directory on remote servers
        put(archive_path, '/tmp/')

        # Create directory structure for deployment
        run("sudo mkdir -p {}".format(newest_version))

        # Extract archive into the specified directory
        run("sudo tar -xzf {} -C {}/".format(archived_file, newest_version))

        # Remove the uploaded archive from /tmp/
        run("sudo rm {}".format(archived_file))

        # Move contents to the proper location using rsync
        run("sudo rsync -a {}/web_static/ {}/".format(newest_version, newest_version))

        # Remove the original 'web_static' directory
        run("sudo rm -rf {}/web_static".format(newest_version))

        # Ensure the required files are present
        run("sudo touch {}/0-index.html".format(newest_version))
        run("sudo touch {}/my_index.html".format(newest_version))

        # Update the symbolic link to the current deployment
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

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

        # Reload Nginx to apply the new configuration
        run("sudo service nginx reload")

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Error deploying: {str(e)}")
        return False

#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

import os
from fabric.api import env, put, run

# Define the remote hosts (web servers)
env.hosts = ['54.160.94.43', '34.203.38.175']
env.user = "ubuntu"  # SSH user for the web servers


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
        archive_name = os.path.basename(archive_path)
        # Remove extension to get the folder name
        archive_folder = archive_name.replace('.tgz', '') \
                                     .replace('.tar.gz', '')

        # Upload archive to /tmp/ directory on remote servers
        put(archive_path, '/tmp/')

        # Create directory structure for deployment
        run(f"mkdir -p /data/web_static/releases/{archive_folder}/")

        # Extract archive into the specified directory
        run(f"tar -xzf /tmp/{archive_name} "
            f"-C /data/web_static/releases/{archive_folder}/")

        # Remove the uploaded archive from /tmp/
        run(f"rm /tmp/{archive_name}")

        # Move contents to the proper location
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(archive_folder,
                                                   archive_folder))

        # Remove the original 'web_static' directory
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            archive_folder))

        # Update the symbolic link to the current deployment
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(archive_folder))

        print("New version deployed successfully!")
        return True

    except Exception as e:
        print(f"Error deploying: {str(e)}")
        return False

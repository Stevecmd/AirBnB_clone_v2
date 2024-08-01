#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers.

This script includes:
- `do_pack`: Creates a .tgz archive from the contents of the web_static folder.
- `do_deploy`: Distributes an archive to the web servers.
- `deploy`: Creates and distributes an archive to the web servers.

Dependencies:
- Fabric
- Cryptography

Notes:
- Suppresses CryptographyDeprecationWarning to avoid cluttering output.

Warnings:
- CryptographyDeprecationWarning: Ignored in this script.

"""

from datetime import datetime
from fabric import *
from fabric.decorators import runs_once
import os
from os.path import exists, isdir
import warnings


# Define the hosts, user, and key filename
env_hosts = ['54.160.94.43', '34.203.38.175']
env_user = "ubuntu"
env_key_filename = "~/.ssh/id_ed25519"


@runs_once
def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The archive path if the archive has been correctly generated.
        None: If the archive was not generated.
    """
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed:
        return None
    return file


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    if not os.path.isfile(archive_path):
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
        return False
    extract_command = (
        "tar -xzf /tmp/{} "
        "-C /data/web_static/releases/{}/".format(file, name)
    )

    # Execute the command and check if it failed
    result = run(extract_command)

    if result.failed:
        return False
    if run("rm /tmp/{}".format(file)).failed:
        return False
    move_command = (
        "mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/".format(name, name)
    )

    # Execute the command and check if it failed
    result = run(move_command)

    if result.failed:
        return False
    remove_command = (
        "rm -rf /data/web_static/releases/{}/"
        "web_static".format(name)
    )

    # Execute the command and check if it failed
    result = run(remove_command)

    if result.failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    link_command = (
        "ln -s /data/web_static/releases/{}/ "
        "/data/web_static/current".format(name)
    )

    if run(link_command).failed:
        return False
    return True


def deploy():
    """
    Creates and distributes an archive to the web servers.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)


if __name__ == "__main__":
    deploy()

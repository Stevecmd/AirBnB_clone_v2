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
from fabric import Connection, task
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
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        os.system("tar -cvzf {} web_static".format(output))
        archive_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archive_size))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        conn = Connection(
            host=env_hosts[0],
            user=env_user,
            connect_kwargs={
                "key_filename": env_key_filename
            }
        )
        conn.put(archive_path, "/tmp/{}".format(file_name))
        conn.run("mkdir -p {}".format(folder_path))
        conn.run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        conn.run("rm -rf /tmp/{}".format(file_name))
        conn.run("mv {}web_static/* {}".format(folder_path, folder_path))
        conn.run("rm -rf {}web_static".format(folder_path))
        conn.run("rm -rf /data/web_static/current")
        conn.run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version is now LIVE!')
        success = True
    except Exception:
        success = False
    return success


def deploy():
    """
    Creates and distributes an archive to the web servers.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()

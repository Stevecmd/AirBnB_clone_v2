#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers
"""

from datetime import datetime
from fabric import Connection
import os
import warnings
from cryptography.utils import CryptographyDeprecationWarning

# Suppress deprecation warnings
warnings.filterwarnings(
    action='ignore',
    category=CryptographyDeprecationWarning
)

# Define the hosts, user, and key filename
env_hosts = ['54.160.94.43', '34.203.38.175']
env_user = "ubuntu"
env_key_filename = "~/.ssh/id_ed25519"


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The archive path if the archive has been correctly generated.
        None: If the archive was not generated.
    """
    os.system("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = os.system(
        "tar -cvzf {} web_static".format(
            archived_f_path
        )
    )

    if t_gzip_archive == 0:
        return archived_f_path
    return None


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

    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        for host in env_hosts:
            conn = Connection(
                host=host,
                user=env_user,
                connect_kwargs={
                    "key_filename": env_key_filename
                }
            )
            conn.put(archive_path, "/tmp/")
            conn.run("mkdir -p {}{}/".format(path, no_ext))
            conn.run(
                "tar -xzf /tmp/{} -C {}{}/".format(
                    file_name,
                    path,
                    no_ext
                )
            )
            conn.run(
                "tar -xzf /tmp/{} -C {}{}/".format(
                    file_name,
                    path,
                    no_ext
                )
            )
            conn.run("rm /tmp/{}".format(file_name))
            conn.run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_ext))
            conn.run("rm -rf {}{}/web_static".format(path, no_ext))
            conn.run("rm -rf /data/web_static/current")
            conn.run(
                "ln -s {}{}/ /data/web_static/current".format(
                    path,
                    no_ext
                )
            )
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


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

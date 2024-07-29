#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from datetime import datetime
from fabric.api import env, local, put, run, lcd, cd
import os

env.hosts = ['54.160.94.43', '34.203.38.175']
env.user = "ubuntu"


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
        return False

    try:
        file_name = os.path.basename(archive_path)
        folder_name = file_name.replace(".tgz", "")
        folder_path = "/data/web_static/releases/{}/".format(folder_name)
        tmp_path = "/tmp/{}".format(file_name)

        put(archive_path, tmp_path)
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf {} -C {}".format(tmp_path, folder_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        run("sudo service nginx reload")

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error deploying: {str(e)}")
        return False


def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Args:
        number (int): The number of archives to keep.
    """
    number = int(number)
    if number == 0:
        number = 1

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]

#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from web_static folder
"""

import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from web_static folder

    Returns:
        str: Path to the generated archive if successful, None otherwise
    """
    if not os.path.exists("versions"):
        os.makedirs("versions")

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    print("Packing web_static to {}".format(archive_path))

    try:
        local("tar -cvzf {} web_static".format(archive_path))
        size = os.path.getsize(archive_path)
        print("web_static packed: {} -> {}Bytes".format(archive_path, size))
        return archive_path
    except Exception as e:
        print("Error packing web_static:", str(e))
        return None

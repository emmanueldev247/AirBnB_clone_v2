#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of web_static
and distributes to my web servers"""

from fabric.api import *
from datetime import datetime
import os.path

env.hosts = ["54.90.15.146", "3.84.239.74"]
env.user = "ubuntu"


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    local("mkdir -p versions")
    now = datetime.utcnow()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    result = local("tar -cvzf {} web_static".format(archive_name))

    if result.succeeded:
        return archive_name
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers
        Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False

    filename = os.path.splitext(os.path.basename(archive_path))[0]

    if put(archive_path, "/tmp/{}".format(filename)).failed:
        return False

    uncmprs_path = "/data/web_static/releases/{}/".format(filename)

    if run("rm -rf {}".format(uncmprs_path)).failed:
        return False

    if run("mkdir -p {}".format(uncmprs_path)).failed:
        return False

    if run("tar -xzf /tmp/{} -C {}".format(filename, uncmprs_path)).failed:
        return False

    if run("rm -rf /tmp/{}".format(archive_path)).failed:
        return False

    if run("mv {}/web_static/* {}".format(uncmprs_path, uncmprs_path)).failed:
        return False

    if run("rm -rf {}/web_static/".format(uncmprs_path)).failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -sf {} /data/web_static/current".format(uncmprs_path)).failed:
        return False
    return True

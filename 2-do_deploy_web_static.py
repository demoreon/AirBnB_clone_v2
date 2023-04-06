#!/usr/bin/python3
"""This script distributes an archive to my web servers
"""

import os
from fabric.api import run, put, env
from datetime import datetime


env.hosts = ['18.209.223.150', '54.174.240.130']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """My do_deploy engine"""

    if not os.path.exists(archive_path):
        return False

    try:
        # Extract the filename
        filename = os.path.basename(archive_path)

        # Define remote paths
        remote_path = "/tmp/{}".format(filename)
        uncompressed_path = "/data/web_static/releases/{}/".format(
            filename.split('.')[0])

        # Upload archive
        put(archive_path, remote_path)

        # Create directories and uncompress archive
        run("sudo mkdir -p {}".format(uncompressed_path))
        run("sudo tar -xzf {} -C {}".format(remote_path, uncompressed_path))

        # Remove archive and move uncompressed files
        run("sudo rm {}".format(remote_path))
        run("sudo mv {}web_static/* {}".format(uncompressed_path, uncompressed_path))
        run("sudo rm -rf {}web_static/".format(uncompressed_path))

        # Update symlink and remove old symlink
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(uncompressed_path))

        return True
    except:
        return False

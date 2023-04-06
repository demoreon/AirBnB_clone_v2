#!/usr/bin/python3
"""This script distributes an archive to my web servers
"""

from fabric.api import *
from datetime import datetime
import os


env.hosts = ['18.209.223.150', '54.174.240.130']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """My do_deploy engine"""

    if os.path.exists(archive_path):
       # using slice to extract the timestamp
       archived_file = archive_path[9:]
       newest_version = "/data/web_static/releases/" + archived_file[:-4]
       archived_file = "/tmp/" + archived_file
       # put used to upload it remotely
       put(archive_path, "/tmp/")
       run("sudo mkdir -p {}".format(newest_version))
       # Uncompresses and delete the .tgz archieve
       run("sudo tar -xzf {} -C {}/".format(archived_file,newest_version))
       # Delete archieve
       run("sudo rm {}".format(archived_file))
       run("sudo mv {}/web_static/* {}".format(newest_version, newest_version))
       run("sudo rm -rf {}/web_static".format(newest_version))
       run("sudo rm -rf /data/web_static/current")
       run("sudo ln -s {} /data/web_static/current".format(newest_version))

       print("New version deployed!")
       return True

    return False

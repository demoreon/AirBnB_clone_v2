#!/usr/bin/python3
""" Function that compresses a folder """


from datetime import datetime
from fabric.api import *
import shlex
import os

env.hosts = ['18.209.223.150', '54.174.240.130']
env.user = "ubuntu"


def do_deploy(archive_path):

    """ Deploys """
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        wn = name.replace('.', ' ')
        wn = shlex.split(wn)
        wn = wn[0]

        releases_path = "/data/web_static/releases/{}/".format(wn)
        tmp_path = "/tmp/{}".format(name)

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        # Uncompresses and delete the .tgz archieve
        run("sudo tar -xzf {} -C {}/".format(archived_file, newest_version))
        # Delete archieve
        run("sudo rm {}".format(archived_file))
        # Move the newest version
        run("sudo mv {}/web_static/*{}".format(newest_version, newest_version))
        # removes the new version
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")

        return True
    except Exception as Er:
        return False

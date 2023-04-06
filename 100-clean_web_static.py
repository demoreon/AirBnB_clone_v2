#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['100.25.19.204', '54.157.159.85']


def do_clean(number=0):
    """Removes unnecessary files

    Args:
        number (int): Number to leave.

    keeps the most and second-most recent archives,

    """
    num = 1 if int(num) == 0 else int(num)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(num)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(num)]
        [run("rm -rf ./{}".format(a)) for a in archives]

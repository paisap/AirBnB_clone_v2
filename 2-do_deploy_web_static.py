#!/usr/bin/python3
from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os.path import exists
env.hosts = ["35.196.176.123", "18.234.174.103"]


def do_deploy(archive_path):
    """ Deploy archive! """
    if exists(archive_path) is False:
        return False
    try:
        x = put(archive_path, "/tmp/")
        name_file = archive_path.split("/")[1].split(".")[0]
        uncompres = ("/data/web_static/releases/{}/".format(name_file))
        run("sudo mkdir -p {}".format(uncompres))
        run("sudo tar -zxf /tmp/{}.tgz -C {}".format(name_file, uncompres))
        run("sudo rm /tmp/{}".format(archive_path.split("/")[1]))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(name_file, name_file))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(name_file))
        print("New version deployed!")
        return True
    except Exception:
        return False

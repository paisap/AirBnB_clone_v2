#!/usr/bin/python3
from fabric.api import local, run, env, put, sudo
from os.path import exists
import datetime
env.hosts = ["35.196.176.123", "18.234.174.103"]
the_path = None


def do_pack():
    """ Compress before sending """
    local("sudo mkdir -p versions")
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    aux = ("versions/web_static_{}.tgz".format(date))
    local("sudo tar -cvzf {} web_static".format(aux))
    return aux


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


def deploy():
    """ deploy all """
    global the_path
    if the_path is None:
        the_path = do_pack()
    if the_path is None:
        reutn False
    return do_deploy(the_path)

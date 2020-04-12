#!/usr/bin/python3
from fabric.api import run
from fabric.api import local
import datetime

def do_pack():
    """ Compress before sending """
    local("sudo mkdir -p versions")
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    aux = ("versions/web_static_{}.tgz".format(date))
    local("sudo tar -cvzf {} web_static".format(aux))
    return aux

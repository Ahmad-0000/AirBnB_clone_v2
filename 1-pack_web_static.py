#!/usr/bin/python3
"""Main fabric file to deploy my static website"""
from fabric.api import *
from datetime import datetime

env.hosts = ['localhost']

now = datetime.now()
year = str(now.year)
month = str(now.month)
day = str(now.day)
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)

name = year + month + day + hour + minute + second


def do_pack():
    """Making a .tgz archive from the static website directory"""
    local("mkdir -p versions")
    local(f"tar -czvf web_static_{name}.tgz web_static")
    local(f"mv web_static_{name}.tgz versions/")

#!/usr/bin/python3
"""Main fabric file to deploy my static website"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['web-1', 'web-2']

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


def do_deploy(archive_path):
    """Deploying the .tgz archive to servers, decompressing it
    and creating a symbolic link to the archive content"""
    if not os.path.isfile(archive_path):
        return False
    if '/' in archive_path:
        archive_name = archive_path.split('/')[-1]
    else:
        archive_name = archive_path
    foldername = archive_name.split('.')[0]
    result = put(local_path=archive_path, remote_path="/tmp/")
    if result.failed:
        return False
    result = run(f"tar -xvf /tmp/{archive_name} -C /data/web_static/releases/")
    if result.failed:
        return False
    new_name = f"/data/web_static/releases/{foldername}"
    if foldername != "web_static":
        result = run(f"mv /data/web_static/releases/web_static {new_name}")
        if result.failed:
            return False
    result = run(f"rm /tmp/{archive_name}")
    if result.failed:
        return False
    result = run("rm -r /data/web_static/current")
    if result.failed:
        return False
    result = run(f"ln -sf {new_name} /data/web_static/")
    if result.failed:
        return False
    result = run(f"mv /data/web_static/{foldername} /data/web_static/current")
    if result.failed:
        return False
    return True

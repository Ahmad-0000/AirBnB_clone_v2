#!/usr/bin/python3
"""Main fabric file to deploy my static website"""
from fabric.api import *
from datetime import datetime
import os

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
    result = run(f"mkdir -p /data/web_static/releases/{foldername}")
    if result.failed:
        return False
    result = run(f"tar -xzf /tmp/{archive_name} -C /data/web_static/releases/{foldername}/")
    if result.failed:
        return False
    result = run(f"rm /tmp/{archive_name}")
    if result.failed:
        return False
    result = run(f"mv /data/web_static/releases/{foldername}/web_static/* /data/web_static/releases/{foldername}")
    if result.failed:
        return False
    result = run(f"rm -rf /data/web_static/releases/{foldername}/web_static")
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/current")
    if result.failed:
        return False
    result = run(f"ln -s /data/web_static/releases{foldername}/ /data/web_static/current")
    if result.failed:
        return False
    print("New version deployed!")
    return True

#!/usr/bin/python3
""" upload tarball and set up server """

from datetime import datetime
from fabric.api import env, run, put, local
from os import path

env.hosts = ['35.196.15.83', '100.26.58.124']


def do_deploy(archive_path):
    ''' deploy tarball and setup env '''

    if path.exists(archive_path):
        put(archive_path, '/tmp/')
    else:
        return False

    tarsplit = archive_path.split('/')
    tarball = tarsplit[-1]
    basename = tarball[:-4]

    run('mkdir -p /data/web_static/releases/{}/'.format(basename))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        .format(tarball, basename))
    run('rm /tmp/{}'.format(tarball))
    run('mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}'.format(basename, basename))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(basename))
    run('rm -rf /data/web_static/current')
    run('ln -sf /data/web_static/releases/{}/ \
        /data/web_static/current'.format(basename))

    return True

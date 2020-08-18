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

    tarball = archive_path.split('/')[1]
    filename = tarball.split('.')[0]

    run('mkdir -p web_static/releases/{}/'.format(filename))
    run('tar -xzf /tmp/{} -C web_static/releases/{}/'
        .format(tarball, filename))
    run('rm -rf /tmp/{}'.format(tarball))
    run('rm /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/\
        /data/web_static/current/'.format(filename))

    return True

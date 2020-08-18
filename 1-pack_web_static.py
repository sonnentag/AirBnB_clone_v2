#!/usr/bin/python3
""" make tarball of web_static """ 
from datetime import datetime
from fabric.api import local


def do_pack():
    ''' tar and compress tarball '''

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    try: 
        local('mkdir -p versions && tar -cvzf versions/web_static_{}.tgz web_static/'.format(now))
        return "versions/web_static_{}.tgz".format(now)
    except:
        return None

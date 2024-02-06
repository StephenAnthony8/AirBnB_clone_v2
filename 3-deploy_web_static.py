#!/usr/bin/python3
"""3-deploy_web_static - creates & distributes archives"""

from datetime import datetime
from fabric.api import *
import os


# env.hosts setting
env.hosts = ['100.26.152.138', '100.25.33.164']


def do_pack():
    """packs web_static directory content into an archive"""
    calendar_day, today = str(datetime.today()).split()
    hour, minute, second = today.split(":")

    label = "{}{}{}{}".format(calendar_day.replace("-", ""),
                              hour,
                              minute,
                              second[: 2])
    command1 = "mkdir -p versions"
    command2 = f"tar -cvzf versions/web_static_{label}.tgz web_static"

    if local(f"{command1} && {command2}").succeeded is True:
        working_dir = f"{os.getcwd()}/versions/web_static_{label}.tgz"

        return (working_dir)

    return (None)


def do_deploy(archive_path):
    """deploys, extracts & configures archive content to servers"""

    # check file path 'archive_path'
    if (os.path.exists(archive_path) and ".tgz" in archive_path):
        # file names & paths
        archive_name = (archive_path[: -4].split('/'))[-1]
        data_filepath = f'/data/web_static/releases/{archive_name}'
        current_filepath = f'/data/web_static/current'

        # commands
        make_data_filepath = f"mkdir -p {data_filepath}/"
        tar_command = f'tar -xzf /tmp/{archive_name}.tgz -C {data_filepath}/'
        rm_archive = f'rm /tmp/{archive_name}.tgz'
        mv_web_static = f'mv {data_filepath}/web_static/* {data_filepath}/'
        rm_web_static = f'rm -rf {data_filepath}/web_static'
        rm_symbolic = f'rm -rf {current_filepath}'
        create_symbolic = f"ln -s {data_filepath}/ {current_filepath}"
        # for shortening
        delete_command = f'{rm_symbolic} && {create_symbolic}'
        # create extraction filepath
        try:
            put(local_path=archive_path, remote_path='/tmp/')

            # upload archive to tmp dir of the web server
            run(f"{make_data_filepath}")

            # uncompress archive to {file_path} && delete archive
            run(f'{tar_command} && {rm_archive}')
            run(f"{mv_web_static} && {rm_web_static}")

            # delete and recreate symbolic link
            run(delete_command)

            return (True)
        except Exception:

            return (False)


def deploy():
    """deploy - creates & distributes archives to the web-servers"""

    # call do_pack & store created archive
    archive_path = do_pack()

    return (do_deploy(archive_path) if archive_path else False)
    # call do_deploy with created archive

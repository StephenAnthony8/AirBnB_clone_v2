#!/usr/bin/python3
""" 2-do_deploy_web_static.py - distributes an archive to web servers"""


from fabric.api import *
import os

# env.hosts setting

env.hosts = ['100.26.152.138', '100.25.33.164']


def do_deploy(archive_path):
    """deploys, extracts & configures archive content to servers"""

    # check file path 'archive_path'
    if (os.path.exists(archive_path) and ".tgz" in archive_path):
        # file names & paths
        archive_name = (archive_path[: -4].split('/'))[-1]
        data_filepath = f'/data/web_static/releases/{archive_name}'
        current_filepath = f'/data/web_static/current'

        # commands
        make_data_filepath = f"mkdir -p {data_filepath}"
        tar_command = f'tar -xzf /tmp/{archive_name}.tgz -C {data_filepath}'
        rm_archive = f'rm -rf /tmp/*.tgz'
        rm_symbolic = f'rm -rf {current_filepath}'
        create_symbolic = f"ln -s {data_filepath} {current_filepath}"
        mv_web_static = f'mv {data_filepath}/web_static/* {data_filepath}/'
        rm_web_static = f'rm -rf {data_filepath}/web_static'

        # create extraction filepath
        if (put(local_path=archive_path, remote_path='/tmp/').succeeded):

            # upload archive to tmp dir of the web server
            if (run(f"{make_data_filepath}").succeeded):

                # uncompress archive to {file_path} && delete archive
                if (run(f'{tar_command} && {rm_archive}').succeeded):
                    run(f"{mv_web_static}")
                    run(rm_web_static)
                    # delete and recreate symbolic link
                    if (run(f'{rm_symbolic} && {create_symbolic} ').succeeded):

                        # return (True) if no errors else (False)
                        return (True)

    return (False)

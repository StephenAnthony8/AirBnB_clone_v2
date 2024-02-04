#!/usr/bin/python3
""" 1-pack_web_static - archives web_static directory & contents """
from datetime import datetime
from fabric.api import local
import os


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

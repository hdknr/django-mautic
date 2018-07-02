#!/usr/bin/env python
import click

import os
name = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'web/app/local_settings.py')
import importlib.util
spec = importlib.util.spec_from_file_location("local_settings", name)
settings = importlib.util.module_from_spec(spec)
spec.loader.exec_module(settings)


@click.group()
def db():
    pass


@db.command()
def createdb():
    SCRIPT = '''CREATE DATABASE {NAME}
DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
GRANT ALL on {NAME}.*
to '{USER}'@'{HOST}'
identified by '{PASSWORD}' WITH GRANT OPTION; '''
    print(SCRIPT.format(**settings.DATABASES['default']))


@db.command()
def dumpschema():
    CMD = 'mysqldump -u {USER} --password={PASSWORD} -h {HOST} {NAME} -d'
    print(CMD.format(**settings.DATABASES['default']))


@db.command()
def dump():
    CMD = 'mysqldump -u {USER} --password={PASSWORD} -h {HOST} {NAME}'
    print(CMD.format(**settings.DATABASES['default']))


def main():
    db()


if __name__ == '__main__':
    main()

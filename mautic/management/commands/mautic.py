import djclick as click
from logging import getLogger
from ...utils import download_geodb

import os
log = getLogger()


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.pass_context
def get_geolite2(ctx):
    download_geodb()


@main.command()
@click.argument('ipaddress')
@click.pass_context
def ip2city(ctx, ipaddress):
    from mautic.utils import resolve_ipaddress
    click.echo(resolve_ipaddress(ipaddress))

import djclick as click
from logging import getLogger
import tarfile
import urllib.request
import os
log = getLogger()


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.pass_context
def get_geolite2(ctx):
    url = 'https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz'
    temp = urllib.request.urlretrieve(url, filename=None)[0]
    with tarfile.open(temp, 'r:gz') as tar:
        for name in tar.getnames():
            if name.endswith('.mmdb'):
                filename = os.path.basename(name)
                with open(filename, "wb") as out:
                    out.write(tar.extractfile(name).read())

@main.command()
@click.argument('ipaddress')
@click.pass_context
def ip2city(ctx, ipaddress):
    from mautic.utils import resolve_ipaddress
    click.echo(resolve_ipaddress(ipaddress))

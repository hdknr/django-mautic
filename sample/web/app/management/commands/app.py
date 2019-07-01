from django.utils import translation
import djclick as click
from logging import getLogger
log = getLogger()

translation.activate('ja')


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.pass_context
def check_migrations(ctx):
    from django.apps import apps  
    latest = apps.get_app_config('app').models
    mautic = apps.get_app_config('mautic').models

    diff = set(key for (key, value) in latest.items()) - \
        set(key for (key, value) in mautic.items())

    if not diff:
        click.echo("no new models")
    else:
        click.echo("new models ---")
        click.echo(diff)
        click.echo([latest[name] for name in diff])
        click.echo('---')

    def _check_fields(name, new, old): 
        diff = set(i.name for i in new._meta.fields) - \
            set(i.name for i in old._meta.fields)
        if diff:
            print(name, "** changed")

        # print(name, new, old)

    for name, model in latest.items():
        if name in mautic:
            _check_fields(name, model, mautic[name])
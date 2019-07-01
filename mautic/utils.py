from django.utils import timezone
from django.conf import settings
import geoip2.database
import glob


def user_to_contact(user):
    '''convert django user to mautic Contact(Lead)'''
    contact = dict(
        firstname=user.first_name,
        lastname=user.last_name,
        email=user.email,
    )
    if user.last_login:
        contact['lastActive'] = user.last_login.strftime('%Y-%m-%d %H:%M:%S')
    return contact


def resolve_ipaddress(ipaddress):
    db = glob.glob(f'{settings.BASE_DIR}/*.mmdb')
    return db and get_city(geoip2.database.Reader(db[0]).city(ipaddress))


def get_city(geocity, lang='ja'):
    res = {}
    res['country'] = dict(
        name=geocity.country.names.get(lang, ''), 
        en=geocity.country.name,
        code=geocity.country.iso_code)

    if geocity.subdivisions:
        res['region'] = dict(
            name=geocity.subdivisions.most_specific.names.get(lang, ''), 
            en=geocity.subdivisions.most_specific.name,
            code=geocity.subdivisions.most_specific.iso_code, 
        )

    if geocity.city:
        res['city'] = dict(
            name=geocity.city.names.get(lang, ''), 
            en=geocity.city.name,
            postl_code=geocity.postal and geocity.postal.code,
        )

    if geocity.location:
        res['location'] = dict(
            tz=geocity.location.time_zone,
            latitude=geocity.location.latitude,
            longitude=geocity.location.longitude,
        )

    return res

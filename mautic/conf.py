from django.conf import settings


class Conf(object):
    base = ''
    user = ''
    password = ''

    @property
    def auth(self):
        return (self.user, self.password)


defaults = type('', (Conf,), getattr(settings, 'MAUTIC',  {}))()

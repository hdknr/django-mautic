import socket
from mautic.utils import resolve_ipaddress


class IpAddresses(object):

    @property
    def hostname(self):
        try:
            name, alias, addresslist = socket.gethostbyaddr(self.ip_address)
            return name
        except:
            pass
    
    @property
    def city(self):
        return resolve_ipaddress(self.ip_address)

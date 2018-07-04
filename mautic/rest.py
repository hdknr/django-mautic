import requests
from . import conf


def get_authorization(headers, auth):
    if headers and 'Authorization' in headers:
        return None
    return auth or conf.defaults.auth 


def endpoint(path, base=None):
    base = base or conf.defaults.base
    return f'{base}/api{path}'


def segment_create(data, base=None, headers=None, auth=None):
    '''
    https://developer.mautic.org/#create-segment
    Return 'list'(Segument) dict if created or refered.
    '''
    auth = get_authorization(headers, auth)
    res = requests.post(
        endpoint('/segments/new', base=base), data=data, headers=headers, auth=auth)

    if res.status_code in [200, 201]:
        data = res.json()
        return data.get('list', None)
    

def segment_contact(command, id, cid, base=None, headers=None, auth=None):
    '''
    Add/Remove Contact from Segment (segment_add_contact or segment_remove_contact)
    https://developer.mautic.org/#add-contact-to-a-segment
    https://developer.mautic.org/#remove-contact-from-a-segment
    '''
    auth = get_authorization(headers, auth)
    res = requests.post(
        endpoint(f'/segments/{id}/contact/{cid}/{command}', base=base), headers=headers, auth=auth)

    if res.status_code in [200]:
        return res.json()


def contact_list(params=None, base=None, headers=None, auth=None):
    '''
    https://developer.mautic.org/#list-contacts
    '''
    auth = get_authorization(headers, auth)
    return requests.get(
        endpoint('/contacts', base=base), params=params, headers=headers, auth=auth)



def contact_create(data, base=None, headers=None, auth=None):
    '''
    https://developer.mautic.org/#create-contact
    Return 'contact' dict if created or refereed.
    '''
    auth = get_authorization(headers, auth)
    res = requests.post(
        endpoint('/contacts/new', base=base), data=data, headers=headers, auth=auth)
    if res.status_code in [200, 201]:
        return res.json().get('contact', None)


def contact_delete(id, base=None, headers=None, auth=None):
    '''
    https://developer.mautic.org/#delete-contact
    Return 'contact' dict if deleted
    '''
    auth = get_authorization(headers, auth)
    res = requests.delete(
        endpoint(f'/contacts/{id}/delete', base=base), headers=headers, auth=auth)

    if res.status_code in [200]:
        return res.json().get('contact', None)


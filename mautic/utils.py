from django.utils import timezone


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
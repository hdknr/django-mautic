#! /usr/bin/env python
from setuptools import setup, find_packages
from glob import glob

NAME = 'django-mautic'
DESCRIPTION = 'Mautic Data Management'
URL = 'https://github.com/hdknr/' + NAME
SCRIPTS = glob('scripts/*.py')
REQUIRES = [
    i.strip() for i in
    open('requirements/pypi.txt').readlines() if i[0] != '#']
README = open('README.md').read()
PACKAGES = [i for i in find_packages() if '.' not in i]
VERSION = getattr(__import__(PACKAGES[0]),  '__version__')

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Simplifed BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


setup(
    license='Simplfied BSD License',
    author='Hideki Nara of LaFoaglia,Inc.',
    author_email='gmail [at] hdknr.com',
    maintainer='LaFoglia,Inc.',
    maintainer_email='gmail [at] hdknr.com',
    classifiers=CLASSIFIERS,
    name=NAME,
    version=VERSION,
    url=URL,
    description=DESCRIPTION,
    download_url=URL,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    long_description=README,
    scripts=SCRIPTS,
    install_requires=REQUIRES,
)

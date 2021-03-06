# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='safire',
    version='0.2.1',
    description='A flexible tool to create and delete Google / GSuite service accounts to be used with shared drives.',
    python_requires='==3.*,>=3.6.1',
    author='88lex',
    keywords='gsuite sas service accounts',
    entry_points={"console_scripts": ["safire = safire.safire:main"]},
    packages=['safire'],
    package_dir={"": "."},
    package_data={
        "safire": [
            "creds/*.json", "creds/*.pickle", "creds/archive/*.json",
            "creds/archive/*.pickle", "data/*.csv", "data/*.xlsx"
        ]
    },
    install_requires=[
        'fire==0.*,>=0.3.1', 'google-api-python-client==1.*,>=1.10.0',
        'google-auth-oauthlib==0.*,>=0.4.1', 'oauth2client==4.*,>=4.1.3',
        'openpyxl==3.*,>=3.0.4', 'pandas==1.*,>=1.0.5',
        'requests==2.*,>=2.24.0', 'uuid==1.*,>=1.30.0'
    ],
)

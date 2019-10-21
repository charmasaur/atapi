
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
    name='atapi',
    version='0.1.0',
    description='Explicitly declare your public API.',
    python_requires='==3.*,>=3.6.0',
    project_urls={'repository': 'https://github.com/charmasaur/atapi'},
    author='Harry Slatyer',
    author_email='harry.slatyer@gmail.com',
    entry_points={'console_scripts': ['atapi = atapi.py']},
    packages=['atapi'],
    package_data={},
    install_requires=[],
    extras_require={'dev': ['dephell==0.*,>=0.7.7', 'fissix==19.*,>=19.2.0']},
)
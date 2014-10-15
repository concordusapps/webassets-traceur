#! /usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from imp import load_source


setup(
    name='webassets-traceur',
    version=load_source('', 'webassets_traceur/_version.py').__version__,
    description='An additional webassets filter to compile ES6 to ES5 '
                'using traceur.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    author='Concordus Applications',
    author_email='support@concordusapps.com',
    url='http://github.com/concordusapps/webassets-traceur',
    packages=find_packages('.'),
    install_requires=[
        'flask >= 0.9.0',
        'webassets >= 0.9.0',
    ]
)

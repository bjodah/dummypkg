#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup_kwargs = {
    'name': 'dummypkg',
    'version': '0.1.0',
    'description': (
        'Dummy package'
    ),
    'license': 'BSD',
    'url': 'https://github.com/bjodah/dummypkg',
    'packages': ['dummypkg', 'dummypkg.tests']
}

if __name__ == '__main__':
    setup(**setup_kwargs)

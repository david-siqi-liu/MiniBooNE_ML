#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup environment and install packages
"""
from setuptools import setup

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements


def setup_package():
    install_requirements = [
        str(package.req) for package in
        parse_requirements('requirements.txt', session=False)
    ]

    setup(
        name='miniboone',
        packages=['miniboone'],
        version='0.1.0',
        description='Capstone project for SCS3253 UoT Machine Learning Winter 2019',
        author='David Siqi Liu',
        install_requires=install_requirements,
        package_data={'': []},
        zip_safe=False
    )


if __name__ == "main":
    setup_package()

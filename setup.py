#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
url: https://github.com/Niger-Volta-LTI
download_url: archive/v{version}.tar.gz

package_data={'iranlowo': ['models/yo_adr_bahdanau_lstm_128_1_1_step_100000_release.pt']}
versioning="distance",  # we start from 0.0.0 using v{major}.{minor}.0

"""


from setuptools import setup
from setuptools import find_packages

setup(
    name="iranlowo",
    version='0.0.4',
    setup_requires="setupmeta",
    license="MIT",
    author="Ruoho Ruotsi ruoho.ruotsi@gmail.com",
    description="Utility package for analysis & (pre)processing of Yorùbá text",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True
)

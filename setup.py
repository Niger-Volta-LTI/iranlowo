#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
url: https://github.com/Niger-Volta-LTI
download_url: archive/v{version}.tar.gz
"""


from setuptools import setup


setup(
    name="iranlowo",
    setup_requires="setupmeta",
    versioning="distance",  # we start from 0.0.0 using v{major}.{minor}.0
    license="MIT",
    author="Ruoho Ruotsi ruoho.ruotsi@gmail.com",
    description="Utility package for analysis & (pre)processing of Yorùbá text",
    include_package_data=True,
    package_data={'iranlowo': ['models/yo_adr_bahdanau_lstm_128_1_1_step_100000_release.pt']}
)

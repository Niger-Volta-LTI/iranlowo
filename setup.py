#!/usr/bin/env python

"""
url: https://github.com/Niger-Volta-LTI
download_url: archive/v{version}.tar.gz
"""


from setuptools import setup


setup(
    name="iranlowo",
    setup_requires="setupmeta",
    # versioning="dev", # iohavoc this probably should be "distance" as we start from 0.0.0 using v{major}.{minor}.0
    license="MIT",
    author="Ruoho Ruotsi ruoho.ruotsi@gmail.com",
    description="Utility package for analysis & (pre)processing of Yorùbá text"
)

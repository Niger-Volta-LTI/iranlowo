#!/usr/bin/env python

"""
url: https://github.com/Niger-Volta-LTI
download_url: archive/v{version}.tar.gz
"""


from setuptools import setup

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="iranlowo",
    version="1.0.0",
    setup_requires="setupmeta",
    versioning="dev",
   	license="MIT",
   	author="Ruoho Ruotsi",
    author_email="ruoho.ruotsi@gmail.com",
    description="Utility package for analysis & (pre)processing of Yorùbá text"
)

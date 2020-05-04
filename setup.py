# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="transfer",
    version="1.0.0",
    url="https://github.com/zhxingy/transfer-py",
    author="zhxingy",
    author_email="zhxingy@aliyun.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["requests", "xmltodict"]
)

#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Zhang Haojie
# Mail:
# Created Time:  2021-1-15 19:17:34
#############################################

from setuptools import setup, find_packages

setup(
    name = "sspku_cat_sphinx_copybutton",      #这里是pip项目发布的名称
    version = "0.1.1",  #版本号，数值大的会优先被pip
    keywords = ("pip", "sspku_cat_sphinx_copybutton","copybutton"),
    description = "sphinx codeblock copybutton extension",
    long_description = "A sphinx codeblock copybutton extension",
    license = "MIT Licence",

    url = "https://github.com/ZhangHaojie077/sspku_cat_sphinx_copybutton",     #项目相关文件地址，一般是github
    author = "ZhangHaojie",
    author_email = "372410616@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy"]          #这个项目需要的第三方库
)


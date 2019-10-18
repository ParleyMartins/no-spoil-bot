#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
No Spoiler bot
===================

"""
from setuptools import setup, find_packages

install_requires = [
    'aiohttp==0.22.4',
    'PyYAML>=3.11',
    'chardet==2.3.0',
    'multidict==1.2.1',
    'telepot==8.3',
    'urllib3==1.24.2',

]


setup(
    name="no-spoiler-bot",
    version='0.1.0',
    author='Parley Martins',
    url='https://github.com/ParleyMartins/no-spoiler-bot',
    entry_points={
        'console_scripts': [
            'bot-run = bot:main',
            'bot-test = bot:test',
        ]},
    description='A Telegram bot to avoid spoilers',
    long_description=__doc__,
    license='GPLv3',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=True,
    test_suite="tests.run.runtests",
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3',
        'Topic :: Utilities',
    ],
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from tempus import __version__

tests_require = [
]

setup(
    name='tempus',
    version=__version__,
    description='tempus is a website that allows you to show a timer in full screen.',
    long_description='''
tempus is a website that allows you to show a timer in full screen.
''',
    keywords='presenting',
    author='Bernardo Heynemann',
    author_email='heynemann@gmail.com',
    url='http://github.com/heynemann/tempus/',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    install_requires=[
        'flask',
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            'tempus=tempus.core:main',
        ],
    },
)

# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '0.1'

setup(
    name='eloquent',
    license='MIT',
    version=__version__,
    description='ActiveRecord ORM for Python.',
    long_description=open('README.rst').read(),
    author='Sébastien Eustace',
    author_email='sebastien.eustace@gmail.com',
    url='https://github.com/sdispater/eloquent',
    download_url='https://github.com/sdispater/eloquent/archive/v%s.tar.gz' % __version__,
    packages=find_packages(),
    install_requires=[],
    tests_require=['nose', 'mock'],
    test_suite='nose.collector',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

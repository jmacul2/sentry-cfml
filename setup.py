#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'sentry>=5.0',
]

f = open('README.rst')
readme = f.read()
f.close()

setup(
    name='sentry-cfml',
    version='0.1.0',
    author='Jay McEntire',
    author_email='jay.mcentire@gmail.com',
    url='http://github.com/jmacul2/sentry-cfml',
    description='A Sentry plugin that adds a custom interface used with the raven-cfml client.',
    long_description=readme,
    license='GNU GPL v3',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'sentry.apps': [
            'sentry_cfml = sentry_cfml',
            ],
        'sentry.plugins': [
            'sentry_cfml = sentry_cfml.plugin:CFMLPlugin'
        ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development'
    ],
)

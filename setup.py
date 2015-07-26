"""
Django-WeRoBot
---------------

Adds WeRoBot support to Django.

:copyright: (c) 2015 by whtsky.
:license: BSD, see LICENSE for more details.

Links
`````

* `documentation <https://django-werobot.readthedocs.org/>`_
"""

from setuptools import setup

setup(
    name='Django-WeRoBot',
    version='0.1.1',
    url='https://github.com/whtsky/Django-WeRoBot',
    license='BSD',
    author='whtsky',
    author_email='whtsky@gmail.com',
    description='Writing WeChat Robot by WeRoBot in Django.',
    long_description=__doc__,
    py_modules=['django_werobot'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'django>=1.4',
        'WeRoBot>=0.3.5'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

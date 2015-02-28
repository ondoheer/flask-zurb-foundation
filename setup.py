"""
Zurb-Foundation-Flask
---------------------

Description goes here...

Links
`````

* `documentation <http://packages.python.org/Flask-Zurb-Foundation>`_
* `development version
  <https://github.com/ondoheer/flask-zurb-foundation>`_

"""
from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Flask-Zurb-Foundation',
    version='0.1.2',
    url='https://github.com/ondoheer/flask-zurb-foundation',
    license='BSD',
    author='ondoheer',
    author_email='ondoheer@gmail.com',
    description='A Foundation Wrapper for Flask',
    long_description=read('README.rst'),
    packages=['flask_zurb_foundation'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
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

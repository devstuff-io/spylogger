import os
from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = open(os.path.join(BASEDIR, 'VERSION')).read().strip()
INSTALL_REQS = parse_requirements('requirements.pip', session=PipSession())

setup(
    name='spylogger',
    packages=['spylogger'],
    version=VERSION,
    include_package_data=True,
    description='Python logging library',
    long_description=open('README.md').read(),
    url='https://github.com/SPSCommerce/spylogger',
    author='meganlkm',
    author_email='mwood@spscommerce.com',
    install_requires=[str(ir.req) for ir in INSTALL_REQS],
    keywords=['logging'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: System :: Logging',
    ]
)

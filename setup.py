from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup

INSTALL_REQS = parse_requirements('requirements.pip', session=PipSession())

setup(
    name='spylogger',
    packages=['spylogger'],
    version='1.0.3',
    include_package_data=True,
    description='Python logging library',
    long_description=open('README.rst').read(),
    url='https://github.com/SPSCommerce/spylogger',
    author='meganlkm',
    author_email='webapps@spscommerce.com',
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

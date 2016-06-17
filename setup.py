from setuptools import setup


setup(
    name='spylogger',
    packages=['spylogger'],
    version='1.0.5',
    include_package_data=True,
    description='Python logging library',
    long_description=open('README.rst').read(),
    url='https://github.com/SPSCommerce/spylogger',
    author='meganlkm',
    author_email='webapps@spscommerce.com',
    install_requires=[],
    keywords=['logging'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: System :: Logging',
    ]
)

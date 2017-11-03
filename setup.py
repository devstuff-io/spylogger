from setuptools import setup

setup(
    name='spylogger',
    packages=['spylogger'],
    version='1.2.1',
    include_package_data=True,
    description='Python logging library',
    long_description=open('README.rst').read(),
    url='https://github.com/devstuff-io/spylogger',
    author='meganlkm',
    author_email='devstuff.io@gmail.com',
    install_requires=[],
    extras_require={
        'pretty': [
            'Pygments',
            'pygments-json',
            'pygments-solarized'
        ]
    },
    keywords=['logging', 'logs', 'pretty'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: System :: Logging',
    ]
)

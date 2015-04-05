try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

import sys
        
extra = {}
if sys.version_info >= (3,):
            extra['use_2to3'] = True

setup(name='sauron',
    version='1.0.0',
    author='Anantha Natarajan S',
    author_email='sananthanatarajan12@gmail.com',
    packages=['sauron'],
    entry_points = {
        'console_scripts': ['sauron=sauron:console_main'],
        },
    test_suite='tests',
    url='https://github.com/sananth12/sauron/',
    description='A simple tool that helps you avoid RSI and CSV.',
    classifiers=[
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities'
                ],
       )

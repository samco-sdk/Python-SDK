from setuptools import setup

setup(name='stocknotebridge',
version='0.0.1',
description='official python library for Stocknote APIs',
url='https://github.com/samco-sdk/Python-SDK',
install_requires=['future', 'requests','websocket','websocket-client'],
author='Samco Securities Limited',
author_email='apisupport@samco.in',
license='MIT License',
packages=['snapi_py_client'],
keywords = ['stocknote api', 'stocknote python sdk','samco api trading','samco algo trading', 'stock markets samco'],
classifiers=[
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
)
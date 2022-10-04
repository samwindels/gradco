#!/usr/bin/env python

import os
import sys
import sysconfig
import numpy as np
from distutils.core import setup, Extension

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

# Common flags for both release and debug builds.
_DEBUG = False

extra_compile_args = sysconfig.get_config_var('CFLAGS').split()
extra_compile_args += ["-Wall", "-Wextra"]
if _DEBUG:
    extra_compile_args += ["-g3", "-O0", "-DDEBUG=%s" % _DEBUG_LEVEL, "-UNDEBUG"]
else:
    extra_compile_args += ["-DNDEBUG", "-O2"]
print(extra_compile_args)

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://gradco.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='gradco',
    version='0.1.0',
    description='Python package to count graphlet adjacencies for graphlets up to four nodes.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Sam Windels',
    author_email='sam.windels@gmail.com',
    url='https://gitlab.bsc.es/swindels/gradco',
    ext_modules=[Extension("gradco", 
                           ["gradco/gradco_module.c"],
                           include_dirs=[np.get_include()],
                           extra_compile_args=extra_compile_args)],
    packages=[
        'gradco',
    ],
    package_dir={'gradco': 'gradco'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='gradco',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)

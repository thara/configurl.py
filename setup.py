# -*- coding: utf-8 -*-
import os
import sys

from configurl import __version__

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
long_description = f.read()
f.close()

setup(
    name="configurl",
    version=__version__,
    description="Utility for loading configuration from URL string",
    license="MIT",
    author="Tomochika Hara",
    author_email='tomochika@isuka.org',
    install_requires=[],
    tests_require=['pytest>=2.5.0'],
    cmdclass={'test': PyTest},
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
    ]
)


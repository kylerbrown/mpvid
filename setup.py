from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import sys
import matplotvid


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='matplotvid',
    version=matplotvid.__version__,
    url='http://github.com/kylerjbrown/matplotvid/',
    license='BSD',
    author='Kyler Brown',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    install_requires=['matplotlib'],
    author_email='kylerjbrown {at} gmail.com',
    description='A quick and dirty matplotlib video library. Uses avconv',
    long_description=long_description,
    packages=['matplotvid'],
    include_package_data=True,
    platforms='any',
    test_suite='matplotvid.test.test_matplotvid',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)

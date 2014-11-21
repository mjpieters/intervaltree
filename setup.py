'''
PyIntervalTree: A mutable, self-balancing interval tree. Queries may be by point, by range overlap, or by range envelopment.

Note that "python setup.py test" invokes pytest on the package. With appropriately
configured setup.cfg, this will check both xxx_test modules and docstrings.

Copyright 2013-2014 Chaim-Leib Halbert

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # import here, because outside the required eggs aren't loaded yet
        sys.exit(pytest.main(self.test_args))


version = '0.3.1'
setup(
    name='PyIntervalTree',
    version=version,
    install_requires=[],
    description='Mutable, self-balancing interval tree',
    long_description=open("README.md").read(),
    classifiers=[ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries',
    ],
    keywords="interval-tree data-structure intervals tree", # Separate with spaces
    author='Chaim-Leib Halbert, Konstantin Tretyakov',
    author_email='chaim.leib.halbert@gmail.com',
    url='https://github.com/chaimleib/PyIntervalTree',
    license="Apache",
    packages=find_packages(exclude=['examples', 'tests', 'test']),
    include_package_data=True,
    zip_safe=True,
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    entry_points={}
)
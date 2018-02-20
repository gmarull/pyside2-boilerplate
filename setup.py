#!/usr/bin/env python

import re
from subprocess import check_call

from setuptools import setup, find_packages
from setuptools import Command


cmdclass = {}


try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass['build_ui'] = build_ui
except ImportError:
    pass

try:
    from sphinx.setup_command import BuildDoc
    cmdclass['build_docs'] = BuildDoc
except ImportError:
    pass


with open('app/__init__.py') as f:
    _version = re.search(r'__version__\s+=\s+\'(.*)\'', f.read()).group(1)


class build_tr(Command):
    """Build translations."""

    description = 'Build translations'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        check_call(['pylupdate5', 'app.pro'])
        check_call(['lrelease', 'app.pro'])


class bdist_app(Command):
    """Custom command to build the application. """

    description = 'Build the application'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        check_call(['pyinstaller', '-y', 'app.spec'])


cmdclass['build_tr'] = build_tr
cmdclass['bdist_app'] = bdist_app


setup(name='app',
      version=_version,
      packages=find_packages(),
      description='PyQt5 Boilerplate',
      author='Gerard Marull-Paretas',
      author_email='gerardmarull@gmail.com',
      license='MIT',
      url='http://www.teslabs.com',
      entry_points={
          'gui_scripts': ['app=app.__main__:main'],
      },
      cmdclass=cmdclass)

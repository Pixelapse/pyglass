#!/usr/bin/env python

# System modules
import sys
import os
import shlex
import subprocess
import shutil
import platform

from os.path import join

# Library modules
try:
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

from distutils.dir_util import copy_tree
from distutils.file_util import copy_file

# Package modules
import pyglass

if sys.version_info[:2] < (2, 7):
  print "Sorry, pyglass requires python version 2.7 or later"
  sys.exit(1)

if platform.system() != 'Darwin':
  print "Sorry, pyglass only runs on OS X"
  sys.exit(1)

LIB_DIR = join('pyglass', 'lib')
BUILD_DIR = join('cocoa', 'build')


def rm_tempdirs():
  ''' Remove temporary build folders '''
  tempdirs = ['build', 'dist', BUILD_DIR, LIB_DIR]
  for tempdir in tempdirs:
    if os.path.exists(tempdir):
      shutil.rmtree(tempdir, ignore_errors=True)


def xcodebuild():
  ''' Build & move the QuickGlass binary to lib '''
  # Build from xcodeproj
  os.chdir('cocoa')
  cmd = 'xcodebuild build'
  subprocess.call(shlex.split(cmd))
  os.chdir('..')


# Compile and copy over libs
rm_tempdirs()
xcodebuild()

os.makedirs(LIB_DIR)
copy_file('cocoa/build/Release/QuickGlass', '%s/QuickGlass' % LIB_DIR)
copy_tree('lib/SketchTool/', '%s/SketchTool/' % LIB_DIR)


setup(
  name='pyglass',
  version=pyglass.__version__,
  url='http://github.com/Pixelapse/pyglass',
  description='Mac OS QuickLook Wrapper',
  long_description=open('README.md').read(),
  author='Shravan Reddy',
  author_email='shravan@pixelapse.com',
  packages=find_packages(),
  package_data={'': ['LICENSE', 'lib/QuickGlass']},
  install_requires=['process'],
  include_package_data=True,
  zip_safe=False,
  license=open('LICENSE').read()
)

rm_tempdirs()

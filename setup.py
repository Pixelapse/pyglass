#!/usr/bin/env python

# System modules
import sys
import os
import shlex
import subprocess
import shutil
import platform

# Library modules
try:
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

# Package modules
import pyglass

if sys.version_info[:2] < (2, 7):
  print "Sorry, pyglass requires python version 2.7 or later"
  sys.exit(1)

if platform.system() != 'Darwin':
  print "Sorry, pyglass only runs on OS X"
  sys.exit(1)

def rm_tempdirs():
  ''' Remove temporary build folders '''
  tempdirs = ['build', 'dist', os.path.join('cocoa', 'build')]
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

  if os.path.exists('pyglass/cocoa/QuickGlass'):
    os.remove('pyglass/cocoa/QuickGlass')

  shutil.move('cocoa/build/Release/QuickGlass', 'pyglass/cocoa/QuickGlass')


# Setup
rm_tempdirs()
xcodebuild()

setup(
  name='pyglass',
  version=pyglass.__version__,
  description='Mac OS QuickLook Wrapper',
  long_description=open('README.md').read(),
  author='Shravan Reddy',
  author_email='shravan@pixelapse.com',
  url="http://github.com/Pixelapse/pyglass",
  packages=find_packages(),
  package_data={'': ['LICENSE', 'cocoa/QuickGlass']},
  include_package_data=True,
  zip_safe=False,
  license=open('LICENSE').read()
)

rm_tempdirs()

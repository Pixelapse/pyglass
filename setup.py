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
  from setuptools import setup
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

  # Move the build binary over
  if not os.path.exists('lib'):
    os.mkdir('lib')

  if os.path.exists('lib/QuickGlass'):
    os.remove('lib/QuickGlass')

  shutil.move('cocoa/build/Release/QuickGlass', 'lib')

rm_tempdirs()
xcodebuild()
rm_tempdirs() # Cleanup after ourselves

packages = ['pyglass']
requires = []

setup(
  name='pyglass',
  version=pyglass.__version__,
  description='Mac OS QuickLook Wrapper',
  long_description=open('README.md').read(),
  author='Shravan Reddy',
  author_email='shravan@pixelapse.com',
  url="http://github.com/Pixelapse/pyglass",
  packages=packages,
  package_data={'': ['LICENSE']},
  install_requires=requires,
  license=open('LICENSE').read()
)

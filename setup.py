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


def mv_lib(src_dir, dest_dir):
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

  src_file = os.path.join(src_dir, 'QuickGlass')
  dest_file = os.path.join(dest_dir, 'QuickGlass')

  if os.path.exists(dest_file):
    os.remove(dest_file)

  shutil.move(src_file, dest_file)


def xcodebuild():
  ''' Build & move the QuickGlass binary to lib '''
  # Build from xcodeproj
  os.chdir('cocoa')
  cmd = 'xcodebuild build'
  subprocess.call(shlex.split(cmd))
  os.chdir('..')

  mv_lib('cocoa/build/Release', 'pyglass/lib')

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
  package_data={'': ['LICENSE', 'lib/QuickGlass']},
  include_package_data=True,
  zip_safe=False,
  license=open('LICENSE').read()
)

rm_tempdirs()

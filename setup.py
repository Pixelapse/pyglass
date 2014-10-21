#!/usr/bin/env python

# System modules
import sys
import os
import shutil
import platform

from os.path import join

# Library modules
try:
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

from distutils.dir_util import copy_tree

# Package modules
if sys.version_info[:2] < (2, 7):
  print "Sorry, pyglass requires python version 2.7 or later"
  sys.exit(1)

if platform.system() != 'Darwin':
  print "Sorry, pyglass only runs on OS X"
  sys.exit(1)


class Dir:
  BUILD = 'build'
  DIST = 'dist'
  COCOA = 'cocoa'
  COCOA_BUILD = join(COCOA, 'build')
  LIB = join('pyglass', 'lib')  # Destination directory for vendor/custom libs
  VENDOR = 'vendor'  # Third-party libraries


def rm_tempdirs():
  ''' Remove temporary build folders '''
  tempdirs = [Dir.BUILD, Dir.COCOA_BUILD, Dir.LIB]
  for tempdir in tempdirs:
    if os.path.exists(tempdir):
      shutil.rmtree(tempdir, ignore_errors=True)


def copy_vendor_libs():
  ''' Copies third party vendor libs into the module '''
  copy_tree('%s/' % Dir.VENDOR, '%s/' % Dir.LIB)


def lib_list():
  ''' Returns the contents of 'pyglass/lib' as a list of 'lib/*' items for package_data '''
  lib_list = []
  for (root, dirs, files) in os.walk(Dir.LIB):
    for filename in files:
      root = root.replace('pyglass/', '')
      lib_list.append(join(root, filename))
  return lib_list

# Compile custom project
rm_tempdirs()

# Copy over libs into Dir.LIB
os.makedirs(Dir.LIB)
copy_vendor_libs()

package_libs = lib_list()

version = '0.1.2'

setup(
  name='pyglass',
  version=version,
  url='http://github.com/Pixelapse/pyglass',
  download_url='https://github.com/Pixelapse/pyglass/tarball/v%s' % version,
  description='Mac OS X File Preview Generator',
  long_description=open('README.md').read(),
  author='Shravan Reddy',
  author_email='shravan@pixelapse.com',
  maintainer='Pixelapse',
  maintainer_email='hello@pixelapse.com',
  packages=find_packages(),
  package_data={'': package_libs},
  install_requires=['pxprocess', 'pyunicode', 'PyPDF2'],
  include_package_data=True,
  zip_safe=False,
  license=open('LICENSE').read()
)

rm_tempdirs()

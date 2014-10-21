# -*- coding: utf-8 -*-
# Default libs
import os
import stat

from os.path import dirname, join, abspath

curr_dir = dirname(abspath(__file__))


def make_executable(path_str):
  ''' Performs the equivalent of `chmod +x` on the file at path_str.
  :returns: path_str if success, else None
  '''
  try:
    mode = os.stat(path_str).st_mode
    os.chmod(path_str, mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
  except Exception as e:
    print 'Exception: %s' % e
    return None
  return path_str


def sketchtool_executable():
  make_executable(join(curr_dir, 'lib', 'SketchTool', 'sketchmigrate'))
  return make_executable(join(curr_dir, 'lib', 'SketchTool', 'sketchtool'))


SKETCHTOOL = sketchtool_executable()
QLMANAGE = join('/usr', 'bin', 'qlmanage')

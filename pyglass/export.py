# -*- coding: utf-8 -*-

import shutil
import subprocess
import shlex

from tempfile import NamedTemporaryFile
from os.path import isdir, exists, join, dirname, abspath

GLASS_LIB = join(dirname(abspath(__file__)), 'lib', 'QuickGlass')

def embedded_preview(src_path):
  if not isdir(src_path):
    return None

  preview_path = join(src_path, 'QuickLook', 'Preview.png')
  if not exists(preview_path):
    return None

  try:
    with NamedTemporaryFile(prefix='pyglass', delete=False) as tempfileobj:
      dest_path = tempfileobj.name
      shutil.copy(preview_path, dest_path)
      return dest_path
  except:
    return None


def thumbnail_preview(src_path, max_width, max_height, format):
  with NamedTemporaryFile(prefix='pyglass', delete=False) as tempfileobj:
    dest_path = tempfileobj.name

    cmd = u'%s -srcPath "%s" -destPath "%s" -maxWidth %f -maxHeight %f -exportFormat "%s"' % \
      (GLASS_LIB, src_path, dest_path, max_width, max_height, format)
    print cmd

    if subprocess.call(shlex.split(cmd)) == 0:
      return dest_path

def thumbnail_preview(src_path):
  """ Returns the path to small thumbnail preview. """
  return None

  try:
    assert(exists(src_path))

    max_width, max_height = 2640, 1520
    export_format = 'png'

    with NamedTemporaryFile(prefix='pyglass', delete=False) as tempfileobj:
      dest_path = tempfileobj.name

    cmd = u'%s -srcPath "%s" -destPath "%s" -maxWidth %f -maxHeight %f -exportFormat "%s"' % \
          (GLASS_LIB, src_path, dest_path, max_width, max_height, export_format)
    print cmd
    assert(subprocess.call(shlex.split(cmd)) == 0)

    assert(exists(dest_path))
    return dest_path
  except:
    return None

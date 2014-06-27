# -*- coding: utf-8 -*-

import shutil
import subprocess
import shlex

from tempfile import NamedTemporaryFile, mkdtemp
from os.path import isdir, exists, join, basename

from .settings import QLMANAGE, QUICKGLASS


def embedded_preview(src_path):
  """ Returns path to temporary copy of embedded QuickLook preview, if it exists """
  try:
    assert(exists(src_path) and isdir(src_path))

    preview_path = join(src_path, 'QuickLook', 'Preview.png')
    assert(exists(preview_path))

    with NamedTemporaryFile(prefix='pyglass', delete=False) as tempfileobj:
      dest_path = tempfileobj.name
      shutil.copy(preview_path, dest_path)
      return dest_path
  except:
    return None


def generator_preview(src_path):
  """ Returns path to the preview created by the generator """
  try:
    assert(exists(src_path))
    src_filename = basename(src_path)

    dest_dir = mkdtemp(prefix='pyglass')
    dest_path = join(dest_dir, '%s.qlpreview' % (src_filename), 'Preview.png')

    cmd = u'%s -p "%s" -o "%s"' % (QLMANAGE, src_path, dest_dir)
    print cmd
    assert(subprocess.call(shlex.split(cmd)) == 0)

    assert(exists(dest_path))
    return dest_path
  except:
    return None


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
          (QUICKGLASS, src_path, dest_path, max_width, max_height, export_format)
    print cmd
    assert(subprocess.call(shlex.split(cmd)) == 0)

    assert(exists(dest_path))
    return dest_path
  except:
    return None

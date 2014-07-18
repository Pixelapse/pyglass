# -*- coding: utf-8 -*-
# Default libs
import shutil

from tempfile import NamedTemporaryFile, mkdtemp
from os.path import isdir, exists, join, basename
from glob import glob

# Library modules
from pxprocess import check_call

# Project modules
from ..settings import QLMANAGE, QUICKGLASS
from ..utils import extension
from ..models import ExportFormat


############################################################
# DONT CALL DIRECTLY
############################################################
def embedded_preview(src_path):
  ''' Returns path to temporary copy of embedded QuickLook preview, if it exists '''
  try:
    assert(exists(src_path) and isdir(src_path))

    preview_list = glob(join(src_path, '[Q|q]uicklook', '[P|p]review.*'))
    assert(preview_list)  # Assert there's at least one preview file
    preview_path = preview_list[0]  # Simplistically, assume there's only one

    with NamedTemporaryFile(prefix='pyglass', suffix=extension(preview_path), delete=False) as tempfileobj:
      dest_path = tempfileobj.name
      shutil.copy(preview_path, dest_path)

    assert(exists(dest_path))
    return dest_path
  except:
    return None


def generator_preview(src_path):
  ''' Returns path to the preview created by the generator '''
  try:
    assert(exists(src_path))

    dest_dir = mkdtemp(prefix='pyglass')
    cmd = [QLMANAGE, '-p', src_path, '-o', dest_dir]
    assert(check_call(cmd) == 0)

    src_filename = basename(src_path)
    dest_list = glob(join(dest_dir, '%s.qlpreview' % (src_filename), '[P|p]review.*'))
    assert(dest_list)

    dest_path = dest_list[0]
    assert(exists(dest_path))

    return dest_path
  except:
    return None


def thumbnail_preview(src_path):
  ''' Returns the path to small thumbnail preview. '''
  try:
    assert(exists(src_path))

    max_width, max_height = '2640', '1520'
    export_format = ExportFormat.PNG

    with NamedTemporaryFile(prefix='pyglass', suffix='.png', delete=False) as tempfileobj:
      dest_path = tempfileobj.name

    cmd = [QUICKGLASS, '-srcPath', src_path, '-destPath', dest_path,
           '-maxWidth', max_width, '-maxHeight', max_height,
           '-exportFormat', export_format]
    assert(check_call(cmd) == 0)

    assert(exists(dest_path))
    return dest_path
  except:
    return None

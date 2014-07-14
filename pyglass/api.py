# -*- coding: utf-8 -*-

from . import quicklook, sketch


def preview(src_path):
  ''' Generates a preview of src_path in the requested format.
  :returns: A list of preview paths, one for each page.
  '''
  previews = []

  if sketch.is_sketchfile(src_path):
    previews = sketch.preview(src_path)

  if not previews:
    previews = quicklook.preview(src_path)

  return previews

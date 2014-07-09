# -*- coding: utf-8 -*-

from . import quicklook, sketch


def preview(src_path):
  ''' Returns the path to a png if single page, pdf if multi-page '''
  preview_path = None

  if sketch.is_sketchfile(src_path):
    preview_path = sketch.preview(src_path)

  if not preview_path:
    preview_path = quicklook.preview(src_path)

  return preview_path

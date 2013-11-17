# -*- coding: utf-8 -*-

from . import export

def export_preview(src_path, max_width=2640, max_height=1520, format="png"):
  preview_path = export.embedded_preview(src_path)
  if preview_path:
    return preview_path

  return export.thumbnail_preview(src_path, max_width, max_height, format)

# -*- coding: utf-8 -*-

from . import export


def export_preview(src_path):
  preview_path = export.embedded_preview(src_path)

  if not preview_path:
    preview_path = export.thumbnail_preview(src_path)

  return preview_path

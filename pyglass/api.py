# -*- coding: utf-8 -*-

from . import quicklook


def export_preview(src_path):
  preview_path = quicklook.embedded_preview(src_path)

  if not preview_path:
    preview_path = quicklook.generator_preview(src_path)

  if not preview_path:
    preview_path = quicklook.thumbnail_preview(src_path)

  return preview_path

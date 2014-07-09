# -*- coding: utf-8 -*-
# Default libs
import os

# Project modules
from .export import embedded_preview, generator_preview, thumbnail_preview


def preview(src_path):
  ''' Returns a file preview. PNG, if single page. PDF, if multi-page. '''
  preview_path = embedded_preview(src_path)

  if not preview_path:
    preview_path = generator_preview(src_path)

  if not preview_path:
    preview_path = thumbnail_preview(src_path)

  if preview_path:
    extension = os.path.splitext(src_path)[1].lower()
    if extension in ['png', 'pdf']:
      return preview_path

  return None

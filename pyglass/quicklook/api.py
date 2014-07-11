# -*- coding: utf-8 -*-
# Default libs

# Installed libs
import magic

# Project modules
from ..models import ExportMimeType
from .export import embedded_preview, generator_preview, thumbnail_preview


def preview(src_path):
  ''' Returns a file preview. PNG, if single page. PDF, if multi-page. '''
  preview_path = embedded_preview(src_path)

  if not preview_path:
    preview_path = generator_preview(src_path)

  if not preview_path:
    preview_path = thumbnail_preview(src_path)

  if preview_path:
    mimetype = magic.from_file(preview_path, mime=True).lower()
    if mimetype in [ExportMimeType.PNG, ExportMimeType.PDF]:
      return preview_path

  return None

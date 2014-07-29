# -*- coding: utf-8 -*-
# Default libs

# Installed libs

# Project modules
from ..models import ExportMimeType
from ..pdf import to_pngs
from ..utils import mimetype
from .export import embedded_preview, generator_preview, thumbnail_preview


def preview(src_path):
  ''' Generates a preview of src_path in the requested format.
  :returns: A list of preview paths, one for each page. Blank list if unsupported.
  '''
  preview = embedded_preview(src_path)

  if not preview:
    preview = generator_preview(src_path)

  if not preview:
    preview = thumbnail_preview(src_path)

  # Ensure the preview is returned in the right format
  if preview:
    if mimetype(preview) in [ExportMimeType.PNG]:
      return [preview]

    if mimetype(preview) in [ExportMimeType.PDF]:
      return to_pngs(preview)

  return []

# -*- coding: utf-8 -*-

# Default libs
import os

# Installed libs
import magic

# Project modules
import pyglass

from tests.helpers import data_file
from tests.test_base import BaseTestCase


############################################################
# BASE CLASSES
############################################################
class PreviewTestCase(BaseTestCase):
  def _test_preview(self, file_path, num_pages=1):
    preview_path = pyglass.preview(file_path)
    self.assertIsNotNone(preview_path)

    mimetype = magic.from_file(preview_path, mime=True).lower()
    if num_pages > 1:
      self.assertEqual(mimetype, pyglass.models.ExportMimeType.PDF)

      from PyPDF2 import PdfFileReader
      pdf_reader = PdfFileReader(preview_path)
      self.assertEqual(pdf_reader.numPages, num_pages)
    else:
      self.assertEqual(mimetype, pyglass.models.ExportMimeType.PNG)

    os.remove(preview_path)


############################################################
# TEST CASES
############################################################
class TestSketchPreview(PreviewTestCase):
  def test_small(self):
    self._test_preview(data_file('sketch/small.sketch'))

  def test_large(self):
    self._test_preview(data_file('sketch/large.sketch'))

  def test_pages(self):
    self._test_preview(data_file('sketch/pages.sketch'), num_pages=3)

  def test_unicode(self):
    self._test_preview(data_file('sketch/unicode.sketch'), num_pages=2)


############################################################
# TEST CASES
############################################################
class TestGrafflePreview(PreviewTestCase):
  def test_pages(self):
    self._test_preview(data_file('graffle/pages.graffle'), num_pages=2)

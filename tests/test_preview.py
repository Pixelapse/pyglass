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
    previews = pyglass.preview(file_path)

    self.assertIsNotNone(previews)
    self.assertIsInstance(previews, list)

    self.assertEqual(len(previews), num_pages)

    for page in previews:
      mimetype = magic.from_file(page, mime=True).lower()
      self.assertEqual(mimetype, pyglass.models.ExportMimeType.PNG)
      os.remove(page)  # Clean up


############################################################
# Sketch
############################################################
class TestSketchPreview(PreviewTestCase):
  def test_small(self):
    self._test_preview(data_file('sketch/small.sketch'))

  def test_large(self):
    self._test_preview(data_file('sketch/large.sketch'))

  def test_pages(self):
    self._test_preview(data_file('sketch/pages.sketch'), num_pages=3)

  def test_artboards(self):
    self._test_preview(data_file('sketch/artboards.sketch'), num_pages=1)

  def test_unicode(self):
    self._test_preview(data_file('sketch/unicode.sketch'), num_pages=2)


############################################################
# Graffle
############################################################
class TestGrafflePreview(PreviewTestCase):
  def test_pages(self):
    self._test_preview(data_file('graffle/pages.graffle'), num_pages=2)

  def test_package(self):
    ''' Test Graffle file saved as package '''
    self._test_preview(data_file('graffle/package.graffle'), num_pages=1)


############################################################
# Plain Text
############################################################
class TestTextPreview(PreviewTestCase):
  def test_plain(self):
    # Verfiy that txt files are unsupported
    self._test_preview(data_file('txt/plain.txt'), num_pages=0)

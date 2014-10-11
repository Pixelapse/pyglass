# -*- coding: utf-8 -*-

# Default libs
import os

# Installed libs

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
      self.assertTrue(os.path.isfile(page))
      mimetype = pyglass.utils.mimetype(page)
      self.assertEqual(mimetype, pyglass.models.ExportMimeType.PNG)
      os.remove(page)  # Clean up


############################################################
# Sketch
############################################################
class TestSketchPreview(PreviewTestCase):
  def test_small(self):
    self._test_preview(data_file('sketch/v3.0/small.sketch'))
    self._test_preview(data_file('sketch/v3.1/small.sketch'))

  def test_large(self):
    self._test_preview(data_file('sketch/v3.0/large.sketch'))
    self._test_preview(data_file('sketch/v3.1/large.sketch'))

  def test_pages(self):
    self._test_preview(data_file('sketch/v3.0/pages.sketch'), num_pages=3)
    self._test_preview(data_file('sketch/v3.1/pages.sketch'), num_pages=3)

  def test_artboards(self):
    self._test_preview(data_file('sketch/v3.0/artboards.sketch'), num_pages=3)
    self._test_preview(data_file('sketch/v3.1/artboards.sketch'), num_pages=3)

  def test_slash_artboards(self):
    self._test_preview(data_file('sketch/v3.0/artboards : slash.sketch'), num_pages=3)
    self._test_preview(data_file('sketch/v3.1/artboards : slash.sketch'), num_pages=3)

  def test_unicode(self):
    self._test_preview(data_file('sketch/v3.0/unicode.sketch'), num_pages=6)
    self._test_preview(data_file('sketch/v3.1/unicode.sketch'), num_pages=6)


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
# Keynote
############################################################
class TestKeynotePreview(PreviewTestCase):
  def test_pages(self):
    # Has 2 pages, only can extract 1 via thumbnail
    self._test_preview(data_file('keynote/pages.key'), num_pages=1)


############################################################
# PowerPoint
############################################################
class TestPowerPointPreview(PreviewTestCase):
  def test_pages(self):
    # Has 2 pages, only can extract 1 via thumbnail
    self._test_preview(data_file('powerpoint/pages.pptx'), num_pages=1)


############################################################
# Word
############################################################
class TestWordPreview(PreviewTestCase):
  def test_pages(self):
    self._test_preview(data_file('word/pages.docx'), num_pages=1)


############################################################
# Excel
############################################################
class TestExcelPreview(PreviewTestCase):
  def test_pages(self):
    self._test_preview(data_file('excel/sheets.xlsx'), num_pages=1)


############################################################
# Plain Text
############################################################
class TestTextPreview(PreviewTestCase):
  def test_plain(self):
    # Verify that we grab the thumbnail from txt files
    self._test_preview(data_file('txt/plain.txt'), num_pages=1)

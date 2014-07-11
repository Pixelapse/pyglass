# -*- coding: utf-8 -*-

# Default libs
import os
import unittest
import time

# Installed libs
import magic

# Project modules
import pyglass

from tests.helpers import data_file


############################################################
# BASE CLASSES
############################################################
class PreviewTestCase(unittest.TestCase):
  def setUp(self):
    print u'******* RUNNING %s TEST *******' % self.id()
    self.time_start = time.time()

  def tearDown(self):
    self.time_elapsed = time.time() - self.time_start
    print u'TIME TO: %s: %s secs' % (self.id(), self.time_elapsed)

  def _test_preview(self, file_path, num_pages=1):
    preview_path = pyglass.preview(file_path)
    self.assertIsNotNone(preview_path)

    mimetype = magic.from_file(preview_path, mime=True).lower()
    if num_pages > 1:
      self.assertEqual(mimetype, pyglass.models.ExportMimeType.PDF)
    else:
      self.assertEqual(mimetype, pyglass.models.ExportMimeType.PNG)

    os.remove(preview_path)


############################################################
# TEST CASES
############################################################
class TestSketch(PreviewTestCase):
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
class TestGraffle(PreviewTestCase):
  def test_pages(self):
    self._test_preview(data_file('graffle/pages.graffle'), num_pages=2)

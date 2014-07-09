# -*- coding: utf-8 -*-

# Default libs
import os
import logging
import unittest
import time

# Installed libs
import magic

# Project modules
import pyglass

from tests.helpers import data_file

logger = logging.getLogger(__name__)


############################################################
# BASE CLASSES
############################################################
class PreviewTestCase(unittest.TestCase):
  def setUp(self):
    logger.info(u'******* RUNNING %s TEST *******' % self.id())
    self.time_start = time.time()

  def tearDown(self):
    self.time_elapsed = time.time() - self.time_start
    logger.info(u'TIME TO: %s: %s secs' % (self.id(), self.time_elapsed))

  def _test_preview(self, file_path, multipage=False):
    preview_path = pyglass.preview(file_path)
    self.assertIsNotNone(preview_path)

    mimetype = magic.from_file(preview_path, mime=True).lower()
    if multipage:
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
    self._test_preview(data_file('sketch/pages.sketch'), multipage=True)

  def test_unicode(self):
    self._test_preview(data_file('sketch/unicode.sketch'), multipage=True)

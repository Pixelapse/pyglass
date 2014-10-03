# -*- coding: utf-8 -*-

# Default libs

# Installed libs

# Project modules
from pyglass.sketch import list_slices, list_artboards, list_pages
from pyglass.sketch import slices, artboards, pages
from pyglass.sketch.models import Slice, Page, Artboard, Rect, Bounds

from tests.helpers import data_file
from tests.test_base import BaseTestCase


############################################################
# TEST CASES
############################################################
class TestSketchExportable(BaseTestCase):
  def _test_bounds(self, bounds):
    ''' Tests for the existence of Bounds class parameters '''
    self.assertIsNotNone(bounds)
    self.assertIsInstance(bounds, Bounds)

    self.assertIsNotNone(bounds.x)
    self.assertIsInstance(bounds.x, float)

    self.assertIsNotNone(bounds.y)
    self.assertIsInstance(bounds.y, float)

    self.assertIsNotNone(bounds.width)
    self.assertIsInstance(bounds.width, float)

    self.assertIsNotNone(bounds.height)
    self.assertIsInstance(bounds.height, float)

  def _test_rect(self, rect):
    ''' Tests for the existence of Rect class parameters '''
    self.assertIsNotNone(rect)
    self.assertIsInstance(rect, Rect)

    self.assertIsNotNone(rect.x)
    self.assertIsInstance(rect.x, float)

    self.assertIsNotNone(rect.y)
    self.assertIsInstance(rect.y, float)

    self.assertIsNotNone(rect.width)
    self.assertIsInstance(rect.width, float)

    self.assertIsNotNone(rect.height)
    self.assertIsInstance(rect.height, float)

  def _test_sketch_exportable(self, exportable):
    ''' Tests for the existence of SketchExportable class parameters '''
    self.assertIsNotNone(exportable.id)
    self.assertIsInstance(exportable.id, unicode)

    self.assertIsNotNone(exportable.name)
    self.assertIsInstance(exportable.name, unicode)

    self.assertIsNotNone(exportable.filename)
    self.assertIsInstance(exportable.filename, basestring)

  def _test_page(self, page):
    ''' Tests for the existence of Page class parameters '''
    self.assertIsNotNone(page)
    self.assertIsInstance(page, Page)
    self._test_sketch_exportable(page)

    self._test_bounds(page.bounds)
    self._test_slices(page.slices)
    self._test_artboards(page.artboards)

  def _test_slice(self, pslice):
    ''' Tests for the existence of Slice class parameters '''
    self.assertIsNotNone(pslice)
    self.assertIsInstance(pslice, Slice)
    self._test_sketch_exportable(pslice)

    self._test_rect(pslice.rect)

  def _test_artboard(self, artboard):
    ''' Tests for the existence of Artboard class parameters '''
    self.assertIsNotNone(artboard)
    self.assertIsInstance(artboard, Artboard)
    self._test_sketch_exportable(artboard)

    self._test_rect(artboard.rect)

  def _test_slices(self, slices):
    self.assertIsNotNone(slices)
    self.assertIsInstance(slices, list)
    for pslice in slices:
      self._test_slice(pslice)

  def _test_artboards(self, artboards):
    self.assertIsNotNone(artboards)
    self.assertIsInstance(artboards, list)
    for artboard in artboards:
      self._test_artboard(artboard)

  def _test_pages(self, pages):
    self.assertIsNotNone(pages)
    self.assertIsInstance(pages, list)

    for page in pages:
      self._test_page(page)

  def _test_list_cmd(self, cmd_result):
    self._test_pages(cmd_result)

  def _test_exportables(self, src_path):
    self._test_list_cmd(list_slices(src_path))
    self._test_slices(slices(src_path))

    self._test_list_cmd(list_artboards(src_path))
    self._test_artboards(artboards(src_path))

    self._test_list_cmd(list_pages(src_path))
    self._test_pages(pages(src_path))

  def test_small(self):
    self._test_exportables(data_file('sketch/v3.0/small.sketch'))
    self._test_exportables(data_file('sketch/v3.1/small.sketch'))

  def test_large(self):
    self._test_exportables(data_file('sketch/v3.0/large.sketch'))
    self._test_exportables(data_file('sketch/v3.1/large.sketch'))

  def test_pages(self):
    self._test_exportables(data_file('sketch/v3.0/pages.sketch'))
    self._test_exportables(data_file('sketch/v3.1/pages.sketch'))

  def test_artboards(self):
    self._test_exportables(data_file('sketch/v3.0/artboards.sketch'))
    self._test_exportables(data_file('sketch/v3.1/artboards.sketch'))

  def test_slash_artboards(self):
    self._test_exportables(data_file('sketch/v3.0/artboards : slash.sketch'))
    self._test_exportables(data_file('sketch/v3.1/artboards : slash.sketch'))

  def test_unicode(self):
    self._test_exportables(data_file('sketch/v3.0/unicode.sketch'))
    self._test_exportables(data_file('sketch/v3.1/unicode.sketch'))

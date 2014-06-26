# -*- coding: utf-8 -*-
# Default libs
import json
import logging

# Library modules
from process import check_output

# Project modules
from .settings import SKETCHTOOL
from .utils import unicode_or_none

logger = logging.getLogger(__name__)


class SketchObject(object):
  ''' Base class for any generic Sketch object '''
  def __unicode__(self):
    return u'<SketchObject>'

  def __str__(self):
    return unicode(self).encode('ascii', 'replace')

  def __repr__(self):
    return unicode(self)


class SketchExportable(SketchObject):
  ''' Base class for any exportable Sketch item, i.e. Pages, Artboards, Slices '''
  def __init__(self, exportable_dict):
    self.id = unicode_or_none(exportable_dict, 'id')
    self.name = unicode_or_none(exportable_dict, 'name')

  def __unicode__(self):
    return u'<SketchExportable (id=\'%s\', name=\'%s\')>' % (self.id, self.name)


class Bounds(SketchObject):
  def __init__(self, bounds_str):
    bounds_list = [float(num) for num in bounds_str.split(',')]

    self.x, self.y = bounds_list[0], bounds_list[1]
    self.width, self.height = bounds_list[2], bounds_list[3]

  def __unicode__(self):
    return u'<Bounds (x=%s, y=%s, width=%s, height=%s)>' % (self.x, self.y, self.width, self.height)


class Rect(SketchObject):
  def __init__(self, rect_dict):
    print 'Rect_dict: %s' % rect_dict
    self.x, self.y = float(rect_dict['x']), float(rect_dict['y'])
    self.width, self.height = float(rect_dict['height']), float(rect_dict['width'])

  def __unicode__(self):
    return u'<Rect (x=%s, y=%s, width=%s, height=%s)>' % (self.x, self.y, self.width, self.height)


class Page(SketchExportable):
  def __init__(self, page_dict):
    self.bounds = Bounds(unicode_or_none(page_dict, 'bounds'))
    self.slices = self.parse_slices(page_dict)
    self.artboards = self.parse_artboards(page_dict)
    super(Page, self).__init__(page_dict)

  def __unicode__(self):
    return u'<Page (id=\'%s\', name=\'%s\', bounds=%s, slices=%s, artboards=%s)>' % \
           (self.id, self.name, self.bounds, self.slices, self.artboards)

  def parse_slices(self, page_dict):
    slices = []
    if 'slices' in page_dict:
      for slice_dict in page_dict['slices']:
        slices.append(Slice(slice_dict))
    return slices

  def parse_artboards(self, page_dict):
    artboards = []
    if 'artboards' in page_dict:
      for artboard_dict in page_dict['artboards']:
        artboards.append(Artboard(artboard_dict))
    return artboards


class Slice(SketchExportable):
  def __init__(self, slice_dict):
    self.rect = Rect(slice_dict['rect'])
    super(Slice, self).__init__(slice_dict)

  def __unicode__(self):
    return u'<Slice (id=\'%s\', name=\'%s\', rect=%s)>' % (self.id, self.name, self.rect)


class Artboard(SketchExportable):
  def __init__(self, artboard_dict):
    self.rect = Rect(artboard_dict['rect'])
    super(Artboard, self).__init__(artboard_dict)

  def __unicode__(self):
    return u'<Artboard (id=\'%s\', name=\'%s\', rect=%s)>' % (self.id, self.name, self.rect)


def execute(cmd):
  ''' Call cmd and return None if any exception occurs '''
  try:
    return check_output(cmd)
  except Exception as e:
    print u'Couldnt execute cmd: %s.\nReason: %s' % (cmd, e)
    return None


def exec_list_cmd(cmd):
  ''' Execute a `sketchtool list` command and parse the output '''
  result = execute(cmd)
  if not result:
    return None

  print u'Raw result: %s' % result
  list_dict = json.loads(result)
  for page_dict in list_dict['pages']:
    page = Page(page_dict)
    print 'Page: %s' % page


def list_slices(src_path):
  cmd = [SKETCHTOOL, 'list', 'slices', src_path]
  return exec_list_cmd(cmd)


def list_artboards(src_path):
  cmd = [SKETCHTOOL, 'list', 'artboards', src_path]
  return exec_list_cmd(cmd)


def list_pages(src_path):
  cmd = [SKETCHTOOL, 'list', 'pages', src_path]
  return exec_list_cmd(cmd)

# def pages_preview(src_path):
#   try:
#     check_call()
#   except Exception as e:
#     print u'Unable to extract pages: %s' % e
#     return None

# -*- coding: utf-8 -*-
from .utils import unicode_or_none
from .parse import parse_artboards, parse_slices


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
    self.width, self.height = float(rect_dict['width']), float(rect_dict['height'])

  def __unicode__(self):
    return u'<Rect (x=%s, y=%s, width=%s, height=%s)>' % (self.x, self.y, self.width, self.height)


class Page(SketchExportable):
  def __init__(self, page_dict):
    self.bounds = Bounds(unicode_or_none(page_dict, 'bounds'))
    self.slices = parse_slices(page_dict)
    self.artboards = parse_artboards(page_dict)
    super(Page, self).__init__(page_dict)

  def __unicode__(self):
    return u'<Page (id=\'%s\', name=\'%s\', bounds=%s, slices=%s, artboards=%s)>' % \
           (self.id, self.name, self.bounds, self.slices, self.artboards)


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

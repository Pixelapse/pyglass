# -*- coding: utf-8 -*-

# Project modules
from ..utils import unicode_or_none
from ..models import Exportable, GenericObject, ExportFormat

from .parse import parse_artboards, parse_slices


############################################################
# DIMENSIONS
############################################################
class Bounds(GenericObject):
  def __init__(self, bounds_str):
    bounds_list = [float(num) for num in bounds_str.split(',')]

    self.x, self.y = bounds_list[0], bounds_list[1]
    self.width, self.height = bounds_list[2], bounds_list[3]

  def __unicode__(self):
    return u'<Bounds (x=%s, y=%s, width=%s, height=%s)>' % (self.x, self.y, self.width, self.height)


class Rect(GenericObject):
  def __init__(self, rect_dict):
    self.x, self.y = float(rect_dict['x']), float(rect_dict['y'])
    self.width, self.height = float(rect_dict['width']), float(rect_dict['height'])

  def __unicode__(self):
    return u'<Rect (x=%s, y=%s, width=%s, height=%s)>' % (self.x, self.y, self.width, self.height)


############################################################
# EXPORTABLE OBJECTS
############################################################
class SketchExportable(Exportable):
  ''' Base class for any exportable Sketch item, i.e. Pages, Artboards, Slices '''
  def __init__(self, filename, exportable_dict):
    self.id = unicode_or_none(exportable_dict, 'id')
    self.name = unicode_or_none(exportable_dict, 'name')
    self.filename = filename  # The file we're exporting from
    super(SketchExportable, self).__init__()

  def __unicode__(self):
    return u'<SketchExportable (id="%s", name="%s")>' % (self.id, self.name)


class Page(SketchExportable):
  def __init__(self, filename, page_dict):
    self.bounds = Bounds(unicode_or_none(page_dict, 'bounds'))
    self.slices = parse_slices(filename, page_dict)
    self.artboards = parse_artboards(filename, page_dict)
    super(Page, self).__init__(filename, page_dict)

  def export(self, export_format=ExportFormat.PNG):
    from .export import export_pages
    pages = export_pages(self.filename, item_id=self.id, export_format=export_format)
    return pages[0] if pages else None

  def __unicode__(self):
    return u'<Page (id="%s", name="%s", bounds=%s, slices=%s, artboards=%s)>' % \
           (self.id, self.name, self.bounds, unicode(self.slices), unicode(self.artboards))


class Slice(SketchExportable):
  def __init__(self, filename, slice_dict):
    self.rect = Rect(slice_dict['rect'])
    super(Slice, self).__init__(filename, slice_dict)

  def export(self, export_format=ExportFormat.PNG):
    from .export import export_slices
    slices = export_slices(self.filename, item_id=self.id, export_format=export_format)
    return slices[0] if slices else None

  def __unicode__(self):
    return u'<Slice (id="%s", name="%s", rect=%s)>' % (self.id, self.name, self.rect)


class Artboard(SketchExportable):
  def __init__(self, filename, artboard_dict):
    self.rect = Rect(artboard_dict['rect'])
    super(Artboard, self).__init__(filename, artboard_dict)

  def export(self, export_format=ExportFormat.PNG):
    from .export import export_artboards
    artboards = export_artboards(self.filename, item_id=self.id, export_format=export_format)
    return artboards[0] if artboards else None

  def __unicode__(self):
    return u'<Artboard (id="%s", name="%s", rect=%s)>' % (self.id, self.name, self.rect)

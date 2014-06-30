# -*- coding: utf-8 -*-


class GenericObject(object):
  ''' Base class for any generic object '''
  def __unicode__(self):
    return u'<GenericObject>'

  def __str__(self):
    return unicode(self).encode('ascii', 'replace')

  def __repr__(self):
    return unicode(self)


class Exportable(GenericObject):
  ''' Any exportable subcomponent of a file. e.g. layers, pages, artboards '''
  def __init__(self):
    self._png_path = None

  def _export(self):
    ''' Overwritten by subclasses to export themselves as pngs '''
    pass

  @property
  def png_path(self):
    if not self._png_path:
      self._png_path = self.export()
    return self._png_path

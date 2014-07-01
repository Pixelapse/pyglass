# -*- coding: utf-8 -*-
# Default libs
import os


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

  def __del__(self):
    self._cleanup()

  def _cleanup(self):
    if self._png_path and os.path.exists(self._png_path):
      os.remove(self._png_path)

  def _export(self):
    ''' Overwritten by subclasses to export themselves as pngs '''
    pass

  @property
  def png_path(self):
    if not self._png_path:
      self._png_path = self._export()
    return self._png_path

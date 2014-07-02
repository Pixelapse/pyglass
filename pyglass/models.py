# -*- coding: utf-8 -*-
# Default libs
import os

# Library modules
from pyunicode import safely_encode


class GenericObject(object):
  ''' Base class for any generic object '''
  def __unicode__(self):
    return u'<GenericObject>'

  def __str__(self):
    return safely_encode(unicode(self))

  def __repr__(self):
    try:
      u = str(self)
    except (UnicodeEncodeError, UnicodeDecodeError):
      u = '[Bad Unicode data]'
    return '<%s: %r>' % (self.__class__.__name__, u)


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

# -*- coding: utf-8 -*-
# Default libs

# Library modules
from pyunicode import safely_encode


class ExportFormat:
  ''' Supported formats '''
  PNG = 'png'
  PDF = 'pdf'


class ExportMimeType:
  ''' Supported mimetypes '''
  PNG = 'image/png'
  PDF = 'application/pdf'


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
  def export(self, export_format=ExportFormat.PNG):
    ''' Overwritten by subclasses to export themselves '''
    pass

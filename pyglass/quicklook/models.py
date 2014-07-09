# -*- coding: utf-8 -*-

# Project modules
from ..models import Exportable, ExportFormat


class QLExportable(Exportable):
  ''' Base class for any exportable QuickLook item '''
  def __init__(self, filename):
    self.filename = filename
    super(QLExportable, self).__init__()

  def __unicode__(self):
    return u'<QLExportable>'


def Page(QLExportable):
  ''' For multi-page files, e.g. if pdf preview '''
  def __init__(self, filename, page_id):
    self.id = page_id
    super(Page, self).__init__(filename)

  def export(self, export_format=ExportFormat.PNG):
    pass

# -*- coding: utf-8 -*-

from process import check_call

from .settings import SKETCHTOOL

def pages_preview(src_path):
  try:

  except Exception as e:
    print u'Unable to extract pages: %s' % e
    return None

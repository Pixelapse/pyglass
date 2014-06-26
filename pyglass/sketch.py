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


class Bounds(object):
  def __init__(self, bounds_str):
    if not bounds_str:
      return

    bounds_list = [float(num) for num in bounds_str.split(',')]

    self.x, self.y = bounds_list[0], bounds_list[1]
    self.width, self.height = bounds_list[2], bounds_list[3]


class Page(object):
  def __init__(self, page_dict):
    self.id = unicode_or_none(page_dict, 'id')
    self.name = unicode_or_none(page_dict, 'name')
    self.bounds = Bounds(unicode_or_none(page_dict, 'bounds'))


def execute(cmd_list):
  try:
    result_dict = json.loads(check_output(cmd_list))
    print 'Result dict; %s' % result_dict
  except Exception as e:
    print u'Couldnt execute cmd: %s.\nReason: %s' % (cmd_list, e)
    return None


def list_slices(src_path):
  cmd = [SKETCHTOOL, 'list', 'slices', src_path]
  return execute(cmd)


def list_artboards(src_path):
  cmd = [SKETCHTOOL, 'list', 'artboards', src_path]
  return execute(cmd)


def list_pages(src_path):
  cmd = [SKETCHTOOL, 'list', 'pages', src_path]
  return execute(cmd)

# def pages_preview(src_path):
#   try:
#     check_call()
#   except Exception as e:
#     print u'Unable to extract pages: %s' % e
#     return None

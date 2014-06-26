# -*- coding: utf-8 -*-
# Default libs
import json
import logging

# Library modules
from process import check_output

# Project modules
from .settings import SKETCHTOOL

logger = logging.getLogger(__name__)


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

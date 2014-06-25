# -*- coding: utf-8 -*-
# Default libs
import json
import logging

# Library modules
from process import call_command

# Project modules
from .settings import SKETCHTOOL

logger = logging.getLogger(__name__)


def list_slices(src_path):
  cmd = '%s list slices %s' % (SKETCHTOOL, src_path)
  print 'Cmd: %s' % cmd
  try:
    slice_dict = json.loads(call_command(cmd))
    logger.info('Slice dict; %s' % slice_dict)
  except Exception as e:
    logger.error(u'Couldnt export slices: %s' % e)
    return None

# def pages_preview(src_path):
#   try:
#     check_call()
#   except Exception as e:
#     print u'Unable to extract pages: %s' % e
#     return None

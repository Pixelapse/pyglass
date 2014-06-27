# -*- coding: utf-8 -*-
# Default libs
import json
import logging

from tempfile import mkdtemp

# Library modules
from process import check_output

# Project modules
from ..settings import SKETCHTOOL
from .parse import parse_pages

logger = logging.getLogger(__name__)


def execute(cmd):
  ''' Call cmd and return None if any exception occurs '''
  try:
    return check_output(cmd)
  except Exception as e:
    print u'Couldnt execute cmd: %s.\nReason: %s' % (cmd, e)
    return None


############################################################
# LIST COMMANDS
############################################################
def list_cmd(cmd):
  ''' Executes a `sketchtool list` command and parse the output '''
  result = execute(cmd)
  if not result:
    return None

  print u'Raw result: %s' % result
  list_dict = json.loads(result)
  pages = parse_pages(list_dict)
  print 'Pages: %s' % pages


def list_slices(src_path):
  cmd = [SKETCHTOOL, 'list', 'slices', src_path]
  return list_cmd(cmd)


def list_artboards(src_path):
  cmd = [SKETCHTOOL, 'list', 'artboards', src_path]
  return list_cmd(cmd)


def list_pages(src_path):
  cmd = [SKETCHTOOL, 'list', 'pages', src_path]
  return list_cmd(cmd)


############################################################
# EXPORT COMMANDS
############################################################
def export_cmd(cmd, dest_dir=None, export_format=None, scale=None):
  ''' Executes a `sketchtool export` command and returns formatted output

  :param export_format: one of type ExportFormat
  :param scale: export scale of type float
  '''
  if not dest_dir:
    dest_dir = mkdtemp(prefix='pyglass')

  cmd.extend(['--output=%s' % dest_dir])

  if export_format:
    cmd.extend(['--formats=%s' % export_format])

  if scale:
    cmd.extend(['--scales=%s' % scale])

  print u'Executing cmd: %s' % cmd
  result = execute(cmd)
  print u'Raw result: %s' % result


def export_slices(src_path, *args, **kwargs):
  cmd = [SKETCHTOOL, 'export', 'slices', src_path]
  return export_cmd(cmd, *args, **kwargs)


def export_artboards(src_path, *args, **kwargs):
  cmd = [SKETCHTOOL, 'export', 'artboards', src_path]
  return export_cmd(cmd, *args, **kwargs)


def export_pages(src_path, *args, **kwargs):
  ''' Exports pages from src_path in dest_dir in given format and scale.

  >>> export_pages('~/example.sketch', dest_dir='~/Desktop/',
                    export_format=ExportFormat.PNG, scale=1.0)
  '''
  cmd = [SKETCHTOOL, 'export', 'pages', src_path]
  return export_cmd(cmd, *args, **kwargs)

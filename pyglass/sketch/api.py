# -*- coding: utf-8 -*-
# Default libs
import json
import logging
import os

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


def is_sketchfile(src_path):
  ''' Returns True if src_path is a sketch file '''
  extension = os.path.splitext(src_path)[1].lower()
  if extension == '.sketch':
    return True
  return False


############################################################
# LIST COMMANDS - PASSTHROUGH TO SKETCHTOOL LIST
############################################################
def list_cmd(cmd, src_path):
  ''' Executes a `sketchtool list` command and parse the output '''
  cmd.extend([src_path])

  result = execute(cmd)
  if not result:
    return None

  print u'Raw result: %s' % result
  list_dict = json.loads(result)
  pages = parse_pages(src_path, list_dict)
  return pages


def list_slices(src_path):
  cmd = [SKETCHTOOL, 'list', 'slices']
  return list_cmd(cmd, src_path)


def list_artboards(src_path):
  cmd = [SKETCHTOOL, 'list', 'artboards']
  return list_cmd(cmd, src_path)


def list_pages(src_path):
  cmd = [SKETCHTOOL, 'list', 'pages']
  return list_cmd(cmd, src_path)


############################################################
# EXPORT COMMANDS - PASSTHROUGH TO SKETCHTOOL EXPORT
############################################################
def export_cmd(cmd, src_path, dest_dir=None, item_id=None, export_format=None, scale=None):
  ''' Executes a `sketchtool export` command and returns formatted output

  :dest_dir: Items are exported at /dest_dir/name@scale.export_format e.g. `~/Desktop/Page 1@2x.png`
  :param export_format: 'png', 'pdf' etc. :type <ExportFormat>
  :param scale: Specify as 1.0, 2.0 etc. :type <float>
  :param item_id: id or name of an Exportable :type <str>
  '''
  cmd.extend([src_path])

  if not dest_dir:
    dest_dir = mkdtemp(prefix='pyglass')

  cmd.extend(['--output=%s' % dest_dir])

  if export_format:
    cmd.extend(['--formats=%s' % export_format])

  if scale:
    cmd.extend(['--scales=%s' % scale])

  if item_id:
    cmd.extend(['--items=%s' % item_id])

  print u'Executing cmd: %s' % cmd
  result = execute(cmd)
  print u'Raw result: %s' % result
  return result


def export_slices(*args, **kwargs):
  cmd = [SKETCHTOOL, 'export', 'slices']
  return export_cmd(cmd, *args, **kwargs)


def export_artboards(*args, **kwargs):
  cmd = [SKETCHTOOL, 'export', 'artboards']
  return export_cmd(cmd, *args, **kwargs)


def export_pages(*args, **kwargs):
  ''' Exports pages from src_path in dest_dir in given format and scale.

  >>> export_pages('~/example.sketch', dest_dir='~/Desktop/',
                    export_format=ExportFormat.PNG, scale=1.0)
  '''
  cmd = [SKETCHTOOL, 'export', 'pages']
  return export_cmd(cmd, *args, **kwargs)


############################################################
# RETURN PAGES, ARTBOARDS, SLICES WITH EXPORTED PNGS
############################################################
def pages(src_path):
  ''' Return pages as flat list '''
  pages = list_pages(src_path)
  print u'Pages: %s' % pages
  return pages


def slices(src_path):
  ''' Return slices as a flat list '''
  pages = list_slices(src_path)
  slices = []
  for page in pages:
    slices.extend(page.slices)
  print u'Slices: %s' % slices
  return slices


def artboards(src_path):
  ''' Return artboards as a flat list '''
  pages = list_artboards(src_path)
  artboards = []
  for page in pages:
    artboards.extend(page.artboards)
  print u'Artboards: %s' % artboards
  return artboards

# -*- coding: utf-8 -*-
# Default libs
import json
import logging

# Project modules
from ..settings import SKETCHTOOL
from ..utils import execute, extension
from .parse import parse_pages

logger = logging.getLogger(__name__)


def is_sketchfile(src_path):
  ''' Returns True if src_path is a sketch file '''
  if extension(src_path) == u'.sketch':
    return True
  return False


############################################################
# LIST COMMANDS - PASSTHROUGH TO SKETCHTOOL LIST
############################################################
def list_cmd(cmd, src_path):
  ''' Executes a `sketchtool list` command and parse the output
  :cmd: A sketchtool list command :type <list>
  :src_path: File to export. :type <str>
  :returns: A list of pages. Artboards & slices are included in the page hierarchy
  '''
  cmd.extend([src_path])

  logger.debug(u'Executing cmd: %s' % cmd)
  result = execute(cmd)
  if not result:
    return None

  logger.debug(u'Raw result: %s' % result)
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
# RETURNS PAGES, ARTBOARDS, SLICES WITH EXPORTED PNGS
############################################################
def pages(src_path):
  ''' Return pages as flat list '''
  pages = list_pages(src_path)
  return pages


def slices(src_path):
  ''' Return slices as a flat list '''
  pages = list_slices(src_path)
  slices = []
  for page in pages:
    slices.extend(page.slices)
  return slices


def artboards(src_path):
  ''' Return artboards as a flat list '''
  pages = list_artboards(src_path)
  artboards = []
  for page in pages:
    artboards.extend(page.artboards)
  return artboards


############################################################
# SIMPLE IMAGE PREVIEW OF FILE
############################################################
def preview(src_path):
  ''' Generates a preview of src_path as PNG.
  :returns: A list of preview paths, one for each page.
  '''
  previews = []
  for page in list_artboards(src_path):
    previews.append(page.export())
    for artboard in page.artboards:
      previews.append(artboard.export())
  return previews

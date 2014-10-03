# -*- coding: utf-8 -*-
# Default libs
import logging
import os

from glob import glob
from tempfile import mkdtemp

# Project modules
from ..settings import SKETCHTOOL
from ..utils import execute

logger = logging.getLogger(__name__)


############################################################
# EXPORT COMMANDS - PASSTHROUGH TO SKETCHTOOL EXPORT
############################################################
def export_cmd(cmd, src_path, dest_dir=None, item_id=None, export_format=None, scale=None):
  ''' Executes a `sketchtool export` command and returns formatted output

  :src_path: File to export. :type <str>
  :dest_dir: Items are exported at /dest_dir/name@scale.export_format e.g. `~/Desktop/Page 1@2x.png`
  :param export_format: 'png', 'pdf' etc. :type <ExportFormat>
  :param scale: Specify as 1.0, 2.0 etc. :type <float>
  :param item_id: id or name of an Exportable :type <str>
  :returns: list of exported item paths
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

  logger.debug(u'Executing cmd: %s' % cmd)
  exported_str = execute(cmd)
  logger.debug(u'Raw result: %s' % exported_str)
  # Raw result is in the form: 'Exported <item-name-1>\nExported <item-name-2>\n'

  exported_items = [os.path.join(dirpath, f)
                    for dirpath, dirnames, files in os.walk(dest_dir)
                    for f in files if f.endswith('.%s' % export_format)]

  return exported_items


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

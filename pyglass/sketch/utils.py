# -*- coding: utf-8 -*-
# Default libs
import logging

from tempfile import NamedTemporaryFile

# Library modules
from process import check_output
from pyunicode import safely_decode

logger = logging.getLogger(__name__)


def execute(cmd):
  ''' Call cmd and return output. return None if any exception occurs '''
  try:
    return safely_decode(check_output(cmd))
  except Exception as e:
    logger.warn(u'Couldnt execute cmd: %s.\nReason: %s' % (cmd, e))
    return None


def unicode_or_none(dictionary, key):
  if dictionary is None or key is None:
    return None
  return None if key not in dictionary or dictionary[key] is None else unicode(dictionary[key])


def stitch_pdfs(pdf_list):
  ''' Merges a series of single page pdfs into one multi-page doc '''
  from PyPDF2 import PdfFileMerger
  pdf_merger = PdfFileMerger()
  for pdf in pdf_list:
    pdf_merger.append(pdf)

  with NamedTemporaryFile(prefix='pyglass', delete=False) as tempfileobj:
    dest_path = tempfileobj.name

  pdf_merger.write(dest_path)
  pdf_merger.close()
  return dest_path

# -*- coding: utf-8 -*-
# Default libs
import os

from tempfile import NamedTemporaryFile
from os.path import exists

# Library modules
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from pxprocess import check_call


############################################################
# PDF CLASSES
############################################################
def stitch_pdfs(pdf_list):
  ''' Merges a series of single page pdfs into one multi-page doc '''
  pdf_merger = PdfFileMerger()
  for pdf in pdf_list:
    pdf_merger.append(pdf)

  with NamedTemporaryFile(prefix='pyglass', suffix='.pdf', delete=False) as tempfileobj:
    dest_path = tempfileobj.name

  pdf_merger.write(dest_path)
  pdf_merger.close()
  return dest_path


def split_pdf(pdf_path):
  ''' Splits a multi-page pdf into a list of single page pdfs '''
  pdf = PdfFileReader(pdf_path)
  pdf_list = []

  for page_num in range(pdf.numPages):
    page = pdf.getPage(page_num)

    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(page)

    with NamedTemporaryFile(prefix='pyglass', suffix='.pdf', delete=False) as tempfileobj:
      pdf_writer.write(tempfileobj)
      page_path = tempfileobj.name

    pdf_list.append(page_path)

  return pdf_list


def to_png(pdf_path):
  ''' Converts a single-page pdf to a png image via the `sips` command
  :returns: Path to the converted png
  '''
  try:
    with NamedTemporaryFile(prefix='pyglass', suffix='.png', delete=False) as tempfileobj:
      png_path = tempfileobj.name

    cmd = ['sips', '-s', 'format', 'png', pdf_path, '--out', png_path]
    assert(check_call(cmd) == 0)

    assert(exists(png_path))
    return png_path
  except:
    return None


def to_pngs(pdf_path):
  ''' Converts a multi-page pdfs to a list of pngs via the `sips` command
  :returns: A list of converted pngs
  '''
  pdf_list = split_pdf(pdf_path)
  pngs = []
  for pdf in pdf_list:
    pngs.append(to_png(pdf))
    os.remove(pdf)  # Clean up
  return pngs

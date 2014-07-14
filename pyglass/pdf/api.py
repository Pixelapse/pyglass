# -*- coding: utf-8 -*-
# Default libs
from tempfile import NamedTemporaryFile


############################################################
# PDF CLASSES
############################################################
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

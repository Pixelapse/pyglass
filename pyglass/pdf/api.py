# -*- coding: utf-8 -*-
# Default libs
from tempfile import NamedTemporaryFile

# Installed libs
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter


############################################################
# PDF CLASSES
############################################################
def stitch_pdfs(pdf_list):
  ''' Merges a series of single page pdfs into one multi-page doc '''
  pdf_merger = PdfFileMerger()
  for pdf in pdf_list:
    pdf_merger.append(pdf)

  with NamedTemporaryFile(prefix='pyglass', delete=False) as tempfileobj:
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

    with NamedTemporaryFile(prefix='pyglass', delete=False) as tempfileobj:
      pdf_writer.write(tempfileobj)
      page_path = tempfileobj.name

    pdf_list.append(page_path)

  return pdf_list

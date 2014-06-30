# -*- coding: utf-8 -*-


def parse_slices(filename, page_dict):
  from .models import Slice
  slices = []
  if 'slices' in page_dict:
    for slice_dict in page_dict['slices']:
      slices.append(Slice(filename, slice_dict))
  return slices


def parse_artboards(filename, page_dict):
  from .models import Artboard
  artboards = []
  if 'artboards' in page_dict:
    for artboard_dict in page_dict['artboards']:
      artboards.append(Artboard(filename, artboard_dict))
  return artboards


def parse_pages(filename, list_dict):
  from .models import Page
  pages = []
  if 'pages' in list_dict:
    for page_dict in list_dict['pages']:
      pages.append(Page(filename, page_dict))
  return pages

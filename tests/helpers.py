# -*- coding: utf-8 -*-

# Default libs
import os

# Project modules


def data_file(src_path_str):
  """ Returns absolute location of data file """
  return os.path.join(os.path.dirname(__file__), 'data', src_path_str)

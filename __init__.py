# -*- coding: utf-8 -*-
"""
pyglass library
~~~~~~~~~~~~~~~~~~~~~

pyglass is a simple wrapper around the cocoa project QuickGlass to extract
QuickLook previews from files.

Basic usage:

   >>> import pyglass
   >>> destPath = pyglass.exportPreview('design_v1.sketch')
   >>> destPath
   /var/folders/fq/xtn_qh1x6c3drpp3ycytx1fr0000gn/T/pyglassY92Xqs

:copyright: (c) 2013 by Pixelapse.
:license: MIT, see LICENSE for more details.

"""
__title__ = 'pyglass'
__version__ = '0.0.1'
__author__ = 'Shravan Reddy'
__license__ = 'MIT'
__copyright__ = 'Copyright 2013 Pixelapse'

from .api import exportPreview

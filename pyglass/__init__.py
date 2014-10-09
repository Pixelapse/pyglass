# -*- coding: utf-8 -*-

"""
pyglass library
~~~~~~~~~~~~~~~~~~~~~

pyglass extracts QuickLook preview images from files.

Basic usage:

   >>> import pyglass
   >>> previews = pyglass.preview('design_v1.sketch')
   >>> previews
   ['/var/folders/fq/xtn_qh1x6c3drpp3ycytx1fr0000gn/T/pyglassY92Xqs',
   '/var/folders/fq/xtn_qh1x6c3drpp3ycytx1fr0000gn/T/pyglassZ34Jab']

:copyright: (c) 2014 by Pixelapse.
:license: MIT, see LICENSE for more details.

"""

__title__ = 'pyglass'
__author__ = 'Shravan Reddy'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Pixelapse'

from .api import preview

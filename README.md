# pyglass: QuickLook in Python

pyglass is a simple wrapper around the cocoa project QuickGlass to extract
QuickLook previews from files.

## Basic Usage

    import pyglass
    destPath = pyglass.export_preview('design_v1.sketch', max_width=250, max_height=320)

## Requirements

  * XCode Command Line Tools

## Installation

    $ python setup.py install

## License
  MIT. See `LICENSE` file.

  Written by Shravan Reddy. Copyright (c) Pixelapse.


# pyglass: Mac OS X File Preview Generator

pyglass is a python wrapper around QuickLook to extract preview images
from files. Additionally, pyglass wraps around SketchTool to generate previews
from [Sketch](bohemiancoding.com/sketch/) files.

## Basic Usage

    import pyglass
    destPath = pyglass.export_preview('design_v1.sketch')

## Requirements
  * Mac OS X 10.7+
  * XCode Command Line Tools

## Installation

    $ python setup.py install

or if using pip:

    pip install "git+git://github.com/Pixelapse/pyglass.git@{version_number}#egg=pyglass"

## License
  MIT. See `LICENSE` file.

  Written by Shravan Reddy. Copyright (c) Pixelapse.


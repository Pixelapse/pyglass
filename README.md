# pyglass: Preview OS X Files

pyglass is a python wrapper around Apple's [QuickLook](https://developer.apple.com/library/mac/documentation/userexperience/conceptual/quicklook_programming_guide/Introduction/Introduction.html) to extract preview images
from common filetypes.

Additionally, pyglass wraps around [SketchTool](http://bohemiancoding.com/sketch/tool/) to generate previews
from [Sketch](bohemiancoding.com/sketch/) files.

## Basic Usage

    >>> import pyglass
    >>> preview_list = pyglass.preview('design_v1.sketch')
    '/var/folders/fq/xtn_qh1x6c3drpp3ycytx1fr0000gn/T/pyglasslTsXov'

## Requirements

### System Requirements
  * Mac OS X 10.7+
  * XCode Command Line Tools

### External Dependencies
  * [Sketch Tool](http://bohemiancoding.com/sketch/tool/)
  * [sips](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/sips.1.html)

## Installation

First install pyglass's dependencies:

    $ pip install -r "https://raw.githubusercontent.com/Pixelapse/pyglass/master/requirements.txt"

Then install the library.

    $ pip install "git+git://github.com/Pixelapse/pyglass.git@{version_number}#egg=pyglass"

## Tests

To run the test suite, execute:

    python setup.py nosetests

## License
  MIT. See `LICENSE` file.

  Written by Shravan Reddy. Copyright (c) Pixelapse.


# pyglass: Preview Mac OS X Documents

pyglass is a python wrapper around Apple's [QuickLook](https://developer.apple.com/library/mac/documentation/userexperience/conceptual/quicklook_programming_guide/Introduction/Introduction.html) to extract preview images
from common filetypes.

Additionally, pyglass wraps around [SketchTool](http://bohemiancoding.com/sketch/tool/) to generate previews
from [Sketch](bohemiancoding.com/sketch/) files.

## Usage

### Basic Previews

    >>> import pyglass
    >>> previews = pyglass.preview('design_v1.sketch')
    >>> previews
     ['/var/folders/fq/xtn_qh1x6c3drpp3ycytx1fr0000gn/T/pyglassY92Xqs.png',
     '/var/folders/fq/xtn_qh1x6c3drpp3ycytx1fr0000gn/T/pyglassZ34Jab.png']

Each preview returned in the list is a PNG, one for each page in the source document.

### Sketch

#### Pages

To get a flat list, use `sketch.pages`. Note that slices and artboards lists within each page are not populated automatically with this command. Use `sketch.list_artboards` and `sketch.list_slices` respectively if you're interested in artboard and slice data.

    >>> pyglass.sketch.pages('/Users/Vayu/Development/src/pyglass/tests/data/sketch/pages.sketch')
    [<Page:
      '<Page (
          id="C10E136D-6E3D-40C9-AA6C-67C456893C6D",
          name="Something",
          bounds=<Bounds (x=-75.0, y=-128.0, width=541.0, height=399.0)>,
          slices=[],
          artboards=[]
       )>'
     >,
    <Page:
      '<Page (
          id="AB21474C-3F41-4531-8433-9E01140E08EC",
          name="Another one",
          bounds=<Bounds (x=-66.0, y=-31.0, width=587.0, height=369.0)>,
          slices=[],
          artboards=[]
       )>'
     >,
    <Page:
      '<Page (
        id="7BEAECDA-21FF-4245-9758-D94A3FDAA9A8",
        name="A third one",
        bounds=<Bounds (x=-99.0, y=-269.0, width=572.0, height=312.0)>,
        slices=[],
        artboards=[]
      )>'
    >]

#### Artboards

To get a flat list, use `sketch.artboards`

    >>> pyglass.sketch.artboards('/Users/Vayu/Development/src/pyglass/tests/data/sketch/artboards.sketch')
    [<Artboard: '<Artboard (
                    id="38BADD7D-C452-4DFD-9054-7939A23902C1",
                    name="Artboard 1",
                    rect=<Rect (x=-101.0, y=-557.0, width=640.0, height=1136.0)>)
                  >'>,
    <Artboard: '<Artboard (
                    id="BFFAD951-2678-4C55-85CB-0B2130BD0392",
                    name="Artboard 2",
                    rect=<Rect (x=639.0, y=-557.0, width=640.0, height=1136.0)>)
                >'>
    ]

To get the entire hierarchy, use `sketch.list_artboards`

    >>> pyglass.sketch.list_artboards('/Users/Vayu/Development/src/pyglass/tests/data/sketch/artboards.sketch')
    [<Page:
      '<Page (
        id="C10E136D-6E3D-40C9-AA6C-67C456893C6D",
        name="Something",
        bounds=<Bounds (x=-131.0, y=-587.0, width=1440.0, height=1196.0)>,
        slices=[],
        artboards=[
          <Artboard: \'<Artboard (
                          id="38BADD7D-C452-4DFD-9054-7939A23902C1",
                          name="Artboard 1",
                          rect=<Rect (x=-101.0, y=-557.0, width=640.0, height=1136.0)>
                        )>\'>,
          <Artboard: \'<Artboard (
                          id="BFFAD951-2678-4C55-85CB-0B2130BD0392",
                          name="Artboard 2",
                          rect=<Rect (x=639.0, y=-557.0, width=640.0, height=1136.0)>
                        )>\'>
        ]
      )>
    '>]

## Requirements

### System Requirements
  * Mac OS X 10.7+
  * [Xcode Command Line Tools](https://developer.apple.com/downloads)

### External Dependencies
  * [Sketch Tool](http://bohemiancoding.com/sketch/tool/)
  * [sips](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/sips.1.html)

## Installation

Simply run:

    $ pip install pyglass

## Tests

To run the test suite, execute:

    python setup.py nosetests

## License
  MIT. See `LICENSE` file.

  Written by Shravan Reddy. Copyright (c) Pixelapse.


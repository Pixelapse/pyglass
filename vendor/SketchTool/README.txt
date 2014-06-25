Sketch Tool

# USAGE

For full help, use the tool:

> sketchtool help


To list slices or artboards:

> sketchtool list slices <doc.sketch>
> sketchtool list artboards <doc.sketch>

This returns JSON information that can be parsed to obtain page and artboard ids.


To export slices or artboards:

> sketchtool export slices <doc.sketch> --output=<folder> --items=<names-or-ids> --scales="1.0, 2.0" --formats="png,pdf,eps,jpg"

> sketchtool export artboards <doc.sketch> --output=<folder> --items=<names-or-ids> --scales="1.0, 2.0" --formats="png,pdf,eps,jpg"

To export arbitrary rectangles from pages at 1.0 and 2.0 scales, as jpgs:

> sketchtool export pages <doc.sketch> --output=<folder> --items=<page-names-or-ids> --bounds="0,0,256,256" --scales="1.0, 2.0" --formats="jpg"


## Specifying Scales and Formats

By default, we export a layer using the options specified for it in the document.

However, specifying --scales, --formats, or both will override all the size/type export settings.

If --formats is specified but not --scales, the default scale "1.0" is used.

If --scales is specified but not --formats, the default format "png" is used.

If neither is specified, we use the size settings in the document itself.

If both are used, we export all combinations. For example --formats="png,eps" --scales="1.0,2.0" will produce four combinations.


## Defaults

All --options can be ommitted. The defaults are:

--formats=
--scales=
--items=(all slices, artboards, pages)
--bounds=(all content on the page)
--output=(current working directory)


# INSTALLATION

You can put the tool anywhere you like (eg /usr/local/bin), but the "sketchtool resources.bundle" file currently has to be in the same directory.


# RELEASE NOTES

1.1.1 Changes

- Added an export layers command which lets you export any layer, even if it's not been marked as exportable in the document.
- Added a --compact option for SVG export which removes some of the extra crud that we would otherwise generate.
- Added a --trimmed option, although it's not respected currently.
- Fixed some bugs relating to the --items option.
- Fixed the app name in generated SVG files.


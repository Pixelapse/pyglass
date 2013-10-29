# -*- coding: utf-8 -*-

# System modules
import tempfile
import subprocess
import shlex

def exportPreview(srcPath, maxWidth=2640, maxHeight=1520, format="png"):
  with tempfile.NamedTemporaryFile(prefix='pyglass', delete=False) as tempfileobj:
    destPath = tempfileobj.name

    cmd = u'lib/QuickGlass -srcPath "%s" -destPath "%s" -maxWidth %f ' \
    '-maxHeight %f -exportFormat "%s"' % (srcPath, destPath, maxWidth, maxHeight, format)
    return_val = subprocess.call(shlex.split(cmd))

    if return_val != 0:
      return None

    return destPath

import os
destPath = exportPreview(
  os.path.expanduser('~/Desktop/Scratchpad/Preview Scripts/Test File.sketch')
)
print u'destPath: %s' % (destPath)

# QuickGlass -srcPath "/Users/Vayu/Desktop/Scratchpad/Preview Scripts/Test File.sketch" -destPath "/Users/Vayu/Desktop/outputfile.png" -exportFormat "png"

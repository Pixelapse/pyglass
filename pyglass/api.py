# -*- coding: utf-8 -*-

# System modules
import os
import tempfile
import subprocess
import shlex

def exportPreview(srcPath, maxWidth=2640, maxHeight=1520, format="png"):
  with tempfile.NamedTemporaryFile(prefix='pyglass', delete=False) as tempfileobj:
    destPath = tempfileobj.name

    quickglassPath = os.path.join(os.path.dirname(__file__), 'lib/QuickGlass')
    cmd = u'%s -srcPath "%s" -destPath "%s" -maxWidth %f ' \
    '-maxHeight %f -exportFormat "%s"' % (quickglassPath, srcPath, destPath, maxWidth, maxHeight, format)
    return_val = subprocess.call(shlex.split(cmd))

    if return_val != 0:
      return None

    return destPath

# -*- coding: utf-8 -*-

# System modules
import os
import tempfile
import subprocess
import shlex

def export_preview(src_path, max_width=2640, max_height=1520, format="png"):
  with tempfile.NamedTemporaryFile(prefix='pyglass', delete=False) as tempfileobj:
    dest_path = tempfileobj.name

    binary_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib/QuickGlass')
    cmd = u'%s -srcPath "%s" -destPath "%s" -maxWidth %f -maxHeight %f -exportFormat "%s"' % \
      (binary_path, src_path, dest_path, max_width, max_height, format)
    print cmd
    return_val = subprocess.call(shlex.split(cmd))

    if return_val != 0:
      return None

    return dest_path

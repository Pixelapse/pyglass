# -*- coding: utf-8 -*-


def unicode_or_none(dictionary, key):
  if dictionary is None or key is None:
    return None
  return None if key not in dictionary or dictionary[key] is None else unicode(dictionary[key])

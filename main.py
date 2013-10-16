# -*- coding: utf-8 -*-

# System modules
import logging


# Library modules
import objc

# Project modules
# from pyglass import utils

# # Enable logging
# utils.initConsoleLogging()

NSObject = objc.lookUpClass('NSObject')
NSAutoreleasePool = objc.lookUpClass('NSAutoreleasePool')
NSDictionary = objc.lookUpClass('NSDictionary')
QuickLook = objc.lookUpClass('QuickLook')

print QuickLook
class PyGlass(NSObject):
  def init(self):
    self = super(PyGlass, self).init()
    return self


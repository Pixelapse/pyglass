# -*- coding: utf-8 -*-

# Default libs
import unittest
import time


############################################################
# BASE CLASSES
############################################################
class BaseTestCase(unittest.TestCase):
  def setUp(self):
    print u'******* RUNNING %s TEST *******' % self.id()
    self.time_start = time.time()

  def tearDown(self):
    self.time_elapsed = time.time() - self.time_start
    print u'TIME TO: %s: %s secs' % (self.id(), self.time_elapsed)

# -*- coding: utf-8 -*-

# System modules
import logging

# Library modules

# Project modules

########################################################################################################
# LOGGING UTILS
########################################################################################################
def initConsoleLogging():
  global CONSOLE_LOGGING_INITIALIZED
  if not CONSOLE_LOGGING_INITIALIZED:
    CONSOLE_LOGGING_INITIALIZED = True
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter(u'%(asctime)s %(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)

    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger().addHandler(console)

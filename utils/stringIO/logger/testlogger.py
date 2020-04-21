# -*- coding: utf-8 -*-

import logging
from logging.config import fileConfig

from utils.configures.paths import LOGCONFIG

fileConfig(LOGCONFIG)
logger = logging.getLogger('tester')


def local_info(msgs):
    msgs = msgs.split('\n')
    for msg in msgs:
        logger.info(msg)


def local_debug(msgs):
    msgs = msgs.split('\n')
    for msg in msgs:
        logger.debug(msg)


def local_error(msgs):
    msgs = msgs.split('\n')
    for msg in msgs:
        logger.error(msg)


INFO = local_info

DEBUG = local_debug

ERROR = local_error

WARN = logger.warn

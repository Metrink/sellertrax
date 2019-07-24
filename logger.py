import logging
import sys

# configure the stream handler
sh = logging.StreamHandler(sys.stderr)
sh.setLevel(logging.DEBUG)
sh.setFormatter(logging.Formatter('[%(asctime)s %(levelname)s] %(filename)s %(lineno)s:\t%(message)s'))

# setup our logger
logger = logging.getLogger('wsgi')
logger.setLevel(logging.INFO)

if len(logger.handlers) == 0:
    logger.addHandler(sh)

# setup the peewee one
peewee_logger = logging.getLogger('peewee')
peewee_logger.setLevel(logging.INFO)

if len(peewee_logger.handlers) == 0:
    peewee_logger.addHandler(sh)


def set_debug():
    logger.setLevel(logging.DEBUG)
    peewee_logger.setLevel(logging.DEBUG)
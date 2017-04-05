# coding=utf-8
import logging, sys, os
from configparser import ConfigParser

__author__ = 'Wes Lanning'


ROOT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
config = ConfigParser()

CONFIG_PATH = os.path.join(os.path.abspath(os.path.join(ROOT_DIR, os.pardir)), 'config.ini')
config.read(CONFIG_PATH)

if not config.sections():
    print('WARNING: No sections in ini file!')

# log stuff for the module
LOGGER_NAME = config['logging']['name']
logger = logging.getLogger(LOGGER_NAME)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if config['logging']['log_to_file']:
    fh = logging.FileHandler(f'{LOGGER_NAME}.log')
    fh.setLevel(config['logging']['file_log_level'])
    fh.setFormatter(formatter)
    logger.addHandler(fh)

if config['logging']['log_to_stdout']:
    ch = logging.StreamHandler()
    ch.setLevel(config['logging']['stdout_log_level'])
    ch.setFormatter(formatter)
    logger.addHandler(ch)



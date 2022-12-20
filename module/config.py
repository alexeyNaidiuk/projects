import logging
import os

from dotenv import load_dotenv

load_dotenv()

ZENNO_KEY = os.environ['ZENNO_KEY']
SERV_HOST = os.environ['SERV_HOST']
CAPMONSTER_HOST = os.environ['CAPMONSTER_HOST']
LOGGING_LEVEL = int(os.environ['LOGGING_LEVEL'])
logging.basicConfig(level=LOGGING_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')

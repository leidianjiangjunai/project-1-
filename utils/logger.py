import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("finbot")
handler = RotatingFileHandler("logs/app.log", maxBytes=10*1024*1024, backupCount=5)
logger.addHandler(handler)
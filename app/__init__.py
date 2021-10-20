from flask import Flask
from app import logger


app = Flask(__name__)
logger.get_custom_logger(app)

from app import routes

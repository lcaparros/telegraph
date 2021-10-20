import logging
from app import app

logger = logging.getLogger(__name__)

@app.route('/')
def hello():
    logger.info("Oh yes!")
    return 'Hello, World!'
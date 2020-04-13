from http.server import HTTPServer
from http_processor import HttpProcessor
import config
from logger import logger


server = HTTPServer((config.SERVER_IP, config.SERVER_PORT), HttpProcessor)
logger.info("Server is running on " + config.SERVER_URL)
server.serve_forever()



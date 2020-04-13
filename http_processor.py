import json
import urllib.request
from http.server import SimpleHTTPRequestHandler
import config
from logger import logger


# requests processing
class HttpProcessor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            return SimpleHTTPRequestHandler.do_GET(self)  # <--- Response with redirection to index.html
        else:
            self.send_response(404)
            logger.info("Invalid endpoint")

    def do_POST(self):
        if self.path == '/':
            logger.info("getting user input")
            content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
            post_data = self.rfile.read(content_length).decode('utf-8').replace("amount=", "")  # <--- Gets user input
            logger.info("Receiving exchange rates")
            req = urllib.request.Request(config.CURRENCY_URL)
            data = urllib.request.urlopen(req).read()
            data_json = json.loads(data.decode("utf-8"))["Valute"]["USD"]["Value"]
            if post_data.isdigit() and float(post_data) >= 0:
                logger.info("result formation")
                value = float(post_data) * float(data_json)
                output_data = {"currency": "USD", "exchange_rate": data_json, "user_input": post_data, "result": value}
                logger.info(output_data)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                logger.info(json.dumps(output_data).encode())
                self.wfile.write(json.dumps(output_data).encode())
                logger.info("result sent")
            else:
                logger.error("Invalid value")
                logger.info(post_data)
                return SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.send_response(404)
            logger.info("Invalid endpoint")

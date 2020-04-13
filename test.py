from http.client import HTTPConnection


def send():
    response = HTTPConnection.request(method="GET", url="https://www.cbr-xml-daily.ru/daily_json.js", self)
    print(response)


if __name__ == "__main__":
    send()
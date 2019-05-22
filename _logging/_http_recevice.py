import logging
from flask import Flask, request

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello():
    data = {}
    for key, value in request.args.items():
        data[key] = value

    logging.info(f"{data['levelname']} {data['levelno']} {data['msg']}")

    return "1"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

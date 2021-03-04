from flask import Flask

app = Flask(__name__)

PORT = 1234


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    print(f'server start at {PORT}')
    app.run(host='0.0.0.0', port=PORT, debug=True)

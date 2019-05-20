from flask import Flask

app = Flask(__name__)


@app.route('/hello>')
def hello(username):
    return 'Hello, World!' + username


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

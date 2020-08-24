from flask import Flask, url_for

app = Flask(__name__)


@app.route('/test_1/<arg>')
def test_1(arg):
    return f"arg {arg}"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)

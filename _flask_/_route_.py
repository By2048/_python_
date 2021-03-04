from flask import Flask, url_for, Blueprint

app = Flask(__name__)


@app.route('/')
def test_1():
    return 'test_1'


app.add_url_rule(rule='/test_1_copy', endpoint='test_1_copy', view_func=test_1)


@app.route('/test_2')
def test_2():
    return "test_2"


@app.route('/test_3', endpoint='test_3_endpoint')
def test_3():
    return "test_3"


user = Blueprint("user", __name__, url_prefix="/user")
file = Blueprint("file", __name__, url_prefix="/file")


@user.route('/article')
def article():
    pass


@file.route('/article')
def article():
    pass


app.register_blueprint(user)
app.register_blueprint(file)

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for("test_1"))
        print(url_for("test_1_copy"))
        print(url_for('test_2'))
        print(url_for('test_3_endpoint'))
        print(url_for('user.article'))
        print(url_for('file.article'))

        print(url_for('test_1', next='/'))
        print(url_for('test_1', username='username'))

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/test_1/<arg>')
def test_1(arg):
    return f"arg {arg} {type(arg)}"


@app.route('/test_2/<string:arg>')
def test_2(arg):
    return f"arg {arg} {type(arg)}"


@app.route('/test_3/<int:arg>')
def test_3(arg):
    return f"arg {arg} {type(arg)}"


@app.route('/test_4/<float:arg>')
def test_4(arg):
    return f"arg {arg} {type(arg)}"


@app.route('/test_5/<path:arg>')
def test_5(arg):
    return f"arg {arg} {type(arg)}"


@app.route('/test_6/<uuid:arg>')
def test_6(arg):
    return f"arg {arg} {type(arg)}"


if __name__ == '__main__':
    client = app.test_client()
    print("test_1", client.get("/test_1/123").data)
    print("test_2", client.get("/test_2/qwe").data)
    print("test_3", client.get("/test_3/123").data)
    print("test_4", client.get("/test_4/1.23").data)
    print("test_5", client.get("/test_5/1/2/3").data)
    print("test_6", client.get("/test_6/d0248364-b3ec-481e-a725-2846c6e72576").data)

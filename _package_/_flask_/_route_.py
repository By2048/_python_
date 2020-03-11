from flask import Flask, url_for

app = Flask(__name__)


# We can use url_for('foo_view') for reverse-lookups in templates or view functions
@app.route('/test1')
def test1():
    pass


# We now specify the custom endpoint named 'bufar'. url_for('bar_view') will fail!
@app.route('/test2', endpoint='test2_endpoint')
def test2():
    pass


app.add_url_rule('/test11', 'test11', test1)

with app.test_request_context('/'):
    print(url_for('test1'))
    print(url_for('test2_endpoint'))
    print(url_for('bar_view'))

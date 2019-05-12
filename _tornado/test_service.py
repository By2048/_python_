# coding=utf-8
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, data):
        self.write(data)
        self.finish()


def make_app():
    return tornado.web.Application([
        (r"/(\d+)/main", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

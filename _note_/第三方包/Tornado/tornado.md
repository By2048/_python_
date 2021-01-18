tornado的视图才有CBV模式，url匹配成功之后先  视图执行顺序为 initialize 、prepare、get/post/put/delete、finish；


import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def initialize(self): #1
        print()

    def prepare(self):
        pass

    def get(self,*args,**kwargs):
        self.write('hello word')

    def post(self, *args, **kwargs):
        pass

    def finish(self, chunk=None):
        pass
        super(self,MainHandler).finish()

        
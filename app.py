import tornado.ioloop
import tornado.web
from src.handlers.DocumentsHandler import DocumentsHandler
from src.handlers.DocumentsHandlerById import DocumentsHandlerById


#class A():
  #  def __init__(self, name):
 #       print("world" + name)


#class B(A):
   # def __init__(self, name):
  #      print("hello")
 #       super().__init__(name)


#B('adwqdwq')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/documents", DocumentsHandler),
        (r"/documents/([0-9]+)", DocumentsHandlerById)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

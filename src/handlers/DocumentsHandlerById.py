import tornado.ioloop
import tornado.web


class DocumentsHandlerById(tornado.web.RequestHandler):
    def get(self, id):
        self.write("Hello, ID" + id)

import tornado.ioloop
import tornado.web


class DocumentsHandler(tornado.web.RequestHandler):
    def get(self, id):
        self.write("Hello, ID" + id)

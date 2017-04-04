import tornado.ioloop
import tornado.web


class DocumentsHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, ALL")

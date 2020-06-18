from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import options,define

import os

define("port", default=8000, type=int)

class IndexHandler(RequestHandler):
   def get(self):
      with open('show.html') as f:
          self.finish(f.read())
 

if __name__ == "__main__":
   app = Application(
       [
           (r"/", IndexHandler),
       ],
       static_path = os.path.join(os.path.dirname(__file__),'static'),debug = True,
template_path = os.path.join(os.path.dirname(__file__),'templates'),
   )
   

   http_server = HTTPServer(app)
   http_server.listen(8000)

   IOLoop.current().start()

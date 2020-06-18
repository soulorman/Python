# encoding: utf-8

from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import options, define

import os
from utils import DBcon

define("port", default=8000, type=int)

class IndexHandler(RequestHandler):

    def get(self):
        if not self.get_cookie('user'):
            return self.render('login.html',errors={})
        
        with open('./templates/show.html') as f:
            self.finish(f.read())


class LoginHandler(RequestHandler):
    def get(self):
        return self.render('login.html',errors={})
        
    def post(self):
        flag = True
        errors = {}
        name = self.get_argument('name')
        password = self.get_argument('password')

        #DBcon.DBconnction()
        if name != 'test':
            errors['name'] = '用户名不存在'
            flag = False

        if password != '123':
            errors['password'] = '密码错误'
            flag = False 
        
        if not flag:
            return self.render('login.html', errors=errors)
        else:
            self.set_cookie('user',name)
            return self.redirect("index", user=name)

if __name__ == "__main__":
    app = Application(
        [
            (r"/", IndexHandler),
            url(r"/login", LoginHandler, name='login'),
            url(r"/index", IndexHandler, name='index'),
        ],
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        debug=True,
    )

    http_server = HTTPServer(app)
    http_server.listen(8000)

    IOLoop.current().start()
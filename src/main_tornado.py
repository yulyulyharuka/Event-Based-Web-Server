import os,sys
import tornado.ioloop
import tornado.web
import tornado.httpserver

class SendFile(tornado.web.RequestHandler):
  def get(self):
    File = open("../testfile/test.txt","r")
    self.write(File.read())
    File.close()

  def post(self):
    File = open("server.txt","r")
    self.write(File.read())
    File.close()

Handlers     = [(r"/",SendFile)]
App_Settings = {"debug":True}
HTTP_Server  = tornado.web.Application(Handlers,**App_Settings)

HTTP_Server.listen(9999)
tornado.ioloop.IOLoop.instance().start()

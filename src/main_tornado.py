import os
import sys
import tornado.ioloop
import tornado.web
import tornado.httpserver

path = None


class SendFile(tornado.web.RequestHandler):
    def get(self):
        global path
        File = open(path, "r")
        self.write(File.read())
        File.close()


def make_app():
    return tornado.web.Application([
        (r"/", SendFile),
    ])


def main(argv):
    global path

    port = int(argv[0])
    path = argv[1]

    app = make_app()

    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main(sys.argv[1:])

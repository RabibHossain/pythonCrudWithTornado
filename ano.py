import tornado.web
import tornado.ioloop

class basicRrequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, This command is executed from backend!")

# def make_app():
#     routes = [
#         (r"/", basicRrequestHandler)
#     ]
#     return tornado.web.Application(routes)

if __name__ == '__main__':
    # app = make_app()
    # routes = [
    #     (r"/", basicRrequestHandler)
    # ]
    app = tornado.web.Application([
        (r"/", basicRrequestHandler)
    ])
    port = 8888
    app.listen(port)
    print(f"Application is ready & listening on port {port}")
    tornado.ioloop.IOLoop.current().start()


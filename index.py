import tornado.web
import tornado.ioloop
import json

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, This command is executed from backend!")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("fruit.html")

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer!")

class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        self.write(f"Welcome {studentName}, the course you are viewing is {courseId}")

class dataRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt","r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))

    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("list.txt", "a")
        fh.write(f"\n{fruit}")
        fh.close()
        self.write(json.dumps({"message": "Data inserted successfully!"}))

if __name__ == '__main__':
    app = tornado.web.Application([
        # (r"/", basicRequestHandler),
        (r"/", listRequestHandler),
        (r"/animal", listRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler),
        (r"/list", dataRequestHandler)
    ])
    port = 8888
    app.listen(port)
    print(f"Application is ready & listening on port {port}")
    tornado.ioloop.IOLoop.current().start()


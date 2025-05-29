import tornado.ioloop
import tornado.web

# Form handler
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("form.html")

    def post(self):
        name = self.get_argument("name")
        email = self.get_argument("email")
        self.write(f"<h3>Hello, {name}! Your email is {email}</h3>")

# App setup
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ],
    template_path="templates")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()

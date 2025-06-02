import pymysql
import tornado.ioloop
import tornado.web

# MySQL database connection
connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='gitpractice',
    cursorclass=pymysql.cursors.DictCursor
)
# Ensure the 'users' table exists
with connection.cursor() as cursor:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
    """)
    connection.commit()
# app.py


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("form.html")

    def post(self):
        name = self.get_argument("name")
        email = self.get_argument("email")

        # Insert into MySQL
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cursor.execute(sql, (name, email))
            connection.commit()

        self.write(f"<h3>Hello, {name}! Your email is {email}. Saved to MySQL.</h3>")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], template_path="templates")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()


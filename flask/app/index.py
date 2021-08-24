from flask import Flask
import env
import database
import models

import os

app = Flask(__name__)
app.config.from_object('config.Config')
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/")
def index():
    return "<h1>Hello, test</h1>"

@app.route("/env")
def get_env():
    return env.flask_db_password

@app.route("/users")
def get_users():
    results = models.User.query.all()

    return "empty"

@app.route("users")
def post_users():
    user = models.User()

    database.db.session.add(user)

@app.route("users", method=["PUT"])
def put_users():
    pass

@app.route("users", method=["DELETE"])
def delete_users():
    pass

if __name__ == "__main__":
    
    database.init_db(app)

    app.run(host="0.0.0.0", port=env.flask_port, debug=env.flask_is_debug)
from flask import Flask
from distutils.util import strtobool
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask</h1>"

print(os.getenv("test") == None)

env = lambda e,d: d if os.getenv(e) == None else os.getenv(e)

flask_port = int(env("FLASK_PORT", "5000"))
flask_is_debug = strtobool(env("FLASK_DEBUG", "true"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=flask_port, debug=flask_is_debug)
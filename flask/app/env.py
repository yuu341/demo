import os
from distutils.util import strtobool

flask_port = int(os.getenv("FLASK_PORT", "5000"))
flask_is_debug = strtobool(os.getenv("FLASK_DEBUG", "true"))

flask_db_host = os.getenv("FLASK_DB_HOST", "localhost")
flask_db_name = os.getenv("FLASK_DB_NAME", "app")
flask_db_user = os.getenv("FLASK_DB_USER", "test")
flask_db_password = os.getenv("FLASK_DB_PASSWORD", "test")
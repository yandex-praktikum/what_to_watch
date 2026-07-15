# opinions_app/__init__.py
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорты в конце — чтобы избежать циклических импортов.
# Модули ниже используют app и db из этого файла.
from . import cli_commands, error_handlers, views  # noqa: E402, F401
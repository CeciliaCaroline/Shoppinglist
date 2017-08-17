from flask import Flask

# Initializing the application
app = Flask(__name__, instance_relative_config=True)

from app import views


# load the config file
app.config.from_object('config')
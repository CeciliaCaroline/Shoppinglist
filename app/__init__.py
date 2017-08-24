from flask import Flask

# Initializing the application
app = Flask(__name__, instance_relative_config=True)

# App configs
app.secret_key = 'ceciliacaroline'
app.config['SESSION_TYPE'] = "filesystem"

# Load the views
from app import views


# load the config file
app.config.from_object('config')
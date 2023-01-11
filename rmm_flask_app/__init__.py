from flask import Flask
app = Flask(__name__)
from rmm_flask_app import routes

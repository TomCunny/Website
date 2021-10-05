from flask import Flask
from app_Blueprint import app_Blueprint

app = Flask(__name__)
app.register_blueprint(app_Blueprint)

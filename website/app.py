from flask import Flask
from app_Blueprint import app_Blueprint

app = Flask(__name__,static_folder="./images")
app.register_blueprint(app_Blueprint)
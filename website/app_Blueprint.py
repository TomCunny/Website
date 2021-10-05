from flask import Blueprint, render_template




app_Blueprint = Blueprint("app_Blueprint",__name__)


@app_Blueprint.route('/')
def index():
    return render_template("index.html")


@app_Blueprint.route('/about')
def about():
    return "<p>about</p>"



@app_Blueprint.route('/products')
def products():
    return render_template("products.html")

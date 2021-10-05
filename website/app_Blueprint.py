from os import name
from flask import Blueprint, render_template, redirect, url_for




app_Blueprint = Blueprint("app_Blueprint",__name__)


@app_Blueprint.route('/')
def index():
    return render_template("index.html")


@app_Blueprint.route('/order')
def about():
    return render_template("order.html")


@app_Blueprint.route('/products')
def products():
    return render_template("products.html")

from flask import Blueprint, render_template




app_Blueprint = Blueprint("app_Blueprint",__name__)

#variable
tshirt = [{'name':'top','price': '15', 'image': 'images/tshirt.jpeg'}]

@app_Blueprint.route('/')
def index():
    return render_template("index.html",tshirt=tshirt)


@app_Blueprint.route('/order')
def about():
    return render_template("order.html")



@app_Blueprint.route('/products')
def products():
    return render_template("products.html")

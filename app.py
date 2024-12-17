from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",titolo='Home page')

@app.route("/products")
def products():
    return render_template("products.html",titolo='Products')

app.run()

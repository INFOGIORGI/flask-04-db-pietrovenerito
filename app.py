from flask import Flask, render_template

app = Flask(__name__)
app.config["MYSQL_HOST"]="138.41.20.102"
app.config["MYSQL_PORT"]="53306"
app.config["MYSQL_DB"]="w3schools"
app.config["MYSQL_USER"]="OSPITE"
app.config["MYSQL_PASSWORD"]="OSPITE"

@app.route("/")
def home():
    return render_template("home.html",titolo='Home page')

@app.route("/products")
def products():
    return render_template("products.html",titolo='Products')

app.run()

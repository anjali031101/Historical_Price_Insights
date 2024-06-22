from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

client = MongoClient('mongodb+srv://tryuser:123123123@scraper.bsq1upl.mongodb.net/?retryWrites=true&w=majority&appName=scraper')
db = client.commodityDB

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/commodities')
def get_all_commodities():
    commodities = db.commodities.find()
    print(commodities)
    return render_template("all_commodities.html", commodities=commodities)

@app.route('/commodity/<name>')
def commodity(name):
    data = db[name].find({})
    return render_template('commodity.html', name=name, data=data)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/search")
def search():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)

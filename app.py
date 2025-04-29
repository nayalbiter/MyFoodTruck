from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/registerFoodCompanyPage')
def go2RegisterCompany():
    return render_template("registerFoodTruckCompany.html")

#@app.route('createCompany')
#def hello():


if __name__ == '__main__':
    app.run(debug=True)
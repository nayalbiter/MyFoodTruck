from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash
from utils.databaseInfo import connectToDatabase
from utils.createCompanyForm import createCompany
from utils.addNewFoodTruckForm import addNewFoodTruck


app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template("index.html")

# Register Food Truck company
@app.route('/registerFoodCompanyPage')
def go2RegisterCompany():
    return render_template("registerFoodTruckCompany.html")


# create company's form
@app.route('/createCompany', methods=['POST'])
def createCompanyForm():
    return createCompany()

#add a new food truck form
@app.route('/addFoodTruckDetails')
def go2FoodTruckDetailsForm():
    return render_template("addNewFoodTruckForm.html")

#create the food truck form
@app.route('/addNewFoodTruck', methods=['POST'])
def createFoodTruckDetailsForm():
    return addNewFoodTruck()


if __name__ == '__main__':
    app.run(debug=True)

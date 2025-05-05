from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash
from utils.databaseInfo import connectToDatabase
from utils.createCompanyForm import createCompany
from utils.addNewFoodTruckForm import insertNewFoodTruck



app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template("index.html")

# Register Food Truck company
@app.route('/registerFoodCompany')
def go2RegisterCompany():
    return render_template("registerFTCompanyForm.html")


# create company's form
@app.route('/getCompanyInformation', methods=['POST'])
def createCompanyForm():
    return createCompany()


#Note: this is the code I did this week:-----------------------------------------------

#show the food truck form   
@app.route('/go2FoodTruckForm')
def go2FoodTruckForm():
    company_id = request.args.get("company_id")
    print(company_id)
    return render_template("addNewFoodTruckForm.html", company_id=company_id)

#add a new food truck to the database
@app.route('/addNewFoodTruck', methods=['POST'])
def addNewFoodTruck():
    return insertNewFoodTruck()

if __name__ == '__main__':
    app.run(debug=True)

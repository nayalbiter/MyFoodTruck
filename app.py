from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash
from utils.databaseInfo import connectToDatabase
from utils.createCompanyForm import createCompany
from utils.addNewFoodTruckForm import addNewFoodTruck
from utils.showCompanyInformation import showCompanyInfo
from utils.getCompanyId import getCompanyIdForFoodTRuckForm


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

#add a new food truck form   
@app.route('/getCompanyId/<int:company_id>')
def getCompanyId():
    return getCompanyIdForFoodTRuckForm() #fix this this should include the company_id or at least get it

#create the food truck form
@app.route('/addNewFoodTruck', methods=['POST'])
def createFoodTruckDetailsForm():
    return addNewFoodTruck()

#show company main page
@app.route('/company/<int:company_id>')
def showCompanyPage(company_id):
    return showCompanyInfo(company_id)


if __name__ == '__main__':
    app.run(debug=True)

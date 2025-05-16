from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager, login_required, logout_user, current_user
from utils.createCompanyForm import createCompany
from utils.addNewFoodTruckForm import insertNewFoodTruck
from utils.getFoodTrucksFromDataBase import getFoodTrucksFromDB
from utils.logInFunction import logInForCompany
from utils.showCompanyMainPage import getCompanyMainPage
from utils.deleteFoodTruckFunction import deleteFoodTruck
from utils.deleteACompanyFunction import deleteCompany
from utils.userModelForAuthentication import User


app = Flask(__name__)

#Authentication for the companies to register and log in 
app.config["SECRET_KEY"] = "key1Used.For9Authentication,Is!Hard#Coded*For%Testing&Purposes0"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "go2LogInPage"

#get the company by id
@login_manager.user_loader
def load_company(company_id):
    return User.get_by_id(company_id)

# Home page
@app.route('/')
def index():
    return render_template("index.html", loggedInCompany = current_user.is_authenticated)

#get the food trucks from the database
@app.route('/fetchFoodTrucks')
def getFoodTrucks():
    return getFoodTrucksFromDB()

# Register Food Truck company
@app.route('/registerFoodCompany')
def go2RegisterCompany():
    return render_template("registerFTCompanyForm.html")

# form to create a new company and then log in into the company main page 
@app.route('/getCompanyInformation', methods=['POST'])
def registerANewCompanyForm():
    return createCompany()

# log in page for food trucks company
@app.route('/logInPage')
def go2LogInPage():
    return render_template("logInCompany.html")

#log in form
@app.route('/logInCompany', methods= ['POST'] )
def logInCompany ():
    return logInForCompany()

#company main page route
@app.route('/foodTruckCompanyMainPage')
@login_required
def go2CompanyMainPageAfterLogIn():
    return getCompanyMainPage()

#show the food truck form
@app.route('/go2FoodTruckForm')
@login_required
def go2FoodTruckForm():
    return render_template("addNewFoodTruckForm.html", company_id=current_user.id)

#add a new food truck to the database
@app.route('/addNewFoodTruck', methods=['POST'])
@login_required
def addNewFoodTruck():
    return insertNewFoodTruck()

#route to delete a company account --> toDo fix the flash messages in both deletes routes
@app.route('/deleteFoodCompany', methods = ['POST'])
@login_required
def deleteFoodTruckCompany():
    return deleteCompany()

#route to edit the company information --> toDo

#route to edit a particular food truck --> toDo

#route to delete a particular food truck
@app.route('/deleteFoodTruck', methods = ['POST'])
@login_required
def deleteAFoodTruck():
    return deleteFoodTruck()

#log out route
@app.route("/logout")
@login_required
def logout():
    print("Logging out:", current_user.company_email)
    logout_user()
    return redirect (url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)

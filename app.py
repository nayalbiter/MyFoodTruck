from flask import Flask, redirect, render_template, request, url_for, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from utils.createCompanyForm import createCompany
from utils.addNewFoodTruckForm import insertNewFoodTruck
from utils.getFoodTrucksFromDataBase import getFoodTrucksFromDB
from utils.userModelForAuthentication import User


app = Flask(__name__)

#Authentication for the companies to register and log in ------------------------------------------!!!!!!!!!!!!!!!!!!!!!
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
    return render_template("index.html")

# log in page for food trucks company
@app.route('/logInPage')
def go2LogInPage():
    return render_template("logInCompany.html")

#log in form
@app.route('/logInCompany', methods= ['POST'] )
def logInCompany ():
    companyEmail = request.form['companyEmail']
    password = request.form['companyPassword']
    
    userForCompany = User.getCompanyEmail(companyEmail)
    
    if not userForCompany:
        print("Company not found for the email:", companyEmail)

    if userForCompany and userForCompany.checkPassword(password):
        print("Accessed")
        login_user(userForCompany)
        return redirect (url_for("go2CompanyMainPageAfterLogIn"))
    else:
        print("NOT Accessed")
        #print("Invalid username or password, try again!")
        return render_template("logInCompany.html")
        
    
#company main page route
@app.route('/foodTruckCompanyMainPage')
@login_required
def go2CompanyMainPageAfterLogIn():
    print("Authenticated?", current_user.is_authenticated)
    print("Company email:", current_user.company_email)
    return render_template("foodCompanyPage.html", company = current_user )


# Register Food Truck company
@app.route('/registerFoodCompany')
def go2RegisterCompany():
    return render_template("registerFTCompanyForm.html")

# form to create a new company and then log in into the company main page  fixing this one!!!
@app.route('/getCompanyInformation', methods=['POST'])
def registerANewCompanyForm():
    return createCompany()

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

#log out route
@app.route("/logout")
@login_required
def logout():
    print("Logging out:", current_user.company_email)
    logout_user()
    session.clear()
    return redirect (url_for("index"))

#get the food trucks from the database
@app.route('/fetchFoodTrucks')
def getFoodTrucks():
    return getFoodTrucksFromDB()

if __name__ == '__main__':
    app.run(debug=True)

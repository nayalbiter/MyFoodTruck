from flask import redirect, render_template, request, url_for
from flask_login import  login_user
from utils.userModelForAuthentication import User

def logInForCompany ():
    companyEmail = request.form['companyEmail']
    password = request.form['companyPassword']
    
    userForCompany = User.getCompanyEmail(companyEmail)
    
    if not userForCompany or not userForCompany.checkPassword(password):
        print("NOT Accessed")
        error = "Invalid email or password. Please try again."
        return render_template("logInCompany.html", error=error)
    
    login_user(userForCompany)
    print("Accessed")
    return redirect(url_for("go2CompanyMainPageAfterLogIn"))
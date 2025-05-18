from flask import redirect, render_template, request, url_for
from flask_login import current_user, logout_user
from utils.userModelForAuthentication import User

def editCompanyDetails():
    
    company_id = request.form.get('company_id')
    
    if current_user.id != int(company_id):
        print("you are not allowed to edit this company account")
        logout_user()
        return redirect (url_for("index"))
    
    company = User.get_by_id(company_id)
    
    return render_template("editCompanyDetails.html", company = company) 
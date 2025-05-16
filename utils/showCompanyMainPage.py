from flask import render_template
from flask_login import current_user
from utils.getFoodTrucksListPerCompany import getFTList

def getCompanyMainPage():
    print("Authenticated?", current_user.is_authenticated)
    print("Company email:", current_user.company_email)
    
    company_id = current_user.id
    
    food_trucks = getFTList(company_id)

    return render_template("foodCompanyPage.html", company = current_user, food_trucks = food_trucks )
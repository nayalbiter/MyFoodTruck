from flask import request, redirect, url_for
from flask_login import current_user, logout_user
from utils.databaseInfo import connectToDatabase
from werkzeug.security import generate_password_hash
import mysql.connector

def updateCompanyInfo():
    company_id = request.form.get('company_id')
    
    if current_user.id != int(company_id):
        print("you are not allowed to edit this company account")
        logout_user()
        return redirect (url_for("index"))
        
    food_description = request.form['foodTruckDescription']
    website = request.form['foodTruckWebsite']
    new_password = request.form['companyPassword'].strip()
    
    try:
        foodTruckDb = connectToDatabase()
        cursor = foodTruckDb.cursor(dictionary=True)
        
        if new_password:
            new_hashed_password = generate_password_hash(new_password)
                
            updateCompanyQuery = """
                update food_companies
                set food_description = %s,
                    business_website = %s,
                    password = %s
                where company_id = %s
            """
            values = (food_description, website, new_hashed_password, company_id)
        else:
            updateCompanyQuery = """
                update food_companies
                set food_description = %s,
                    business_website = %s
                where company_id = %s
            """
            values = (food_description, website, company_id)
        
        cursor.execute(updateCompanyQuery, values)
        foodTruckDb.commit()
        print("the food company was updated successfully")
    
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    
    finally:
        cursor.close()
        foodTruckDb.close()
        
    return redirect(url_for("go2CompanyMainPageAfterLogIn"))     
    
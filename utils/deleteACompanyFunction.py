from flask import flash, redirect, request, url_for
from flask_login import current_user, logout_user
from utils.databaseInfo import connectToDatabase
import mysql.connector

def deleteCompany():
    
    company_id = request.form.get('company_id')
    print(f"this is the company_id : {company_id}")
    
    if not company_id or int(company_id) != current_user.id:
        print("there is not company id, not working")
        #flash("You are not allowed to delete this account.", "danger")
        logout_user()
        return redirect(url_for("index"))
    
    deleteFoodCompanyQuery = "delete from food_companies where company_id = %s "
    
    try:
        dataBase = connectToDatabase()
        cursor = dataBase.cursor(dictionary=True)
        cursor.execute(deleteFoodCompanyQuery, (current_user.id,))
        dataBase.commit()
        logout_user()
        print("the company was deleted successfully")
        #flash("Your company and its food trucks have been deleted.", "success")
        return redirect(url_for('index'))
        
    
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        #flash(f"An error occurred while deleting this food company: {err}", "danger")
        return redirect(url_for('go2CompanyMainPageAfterLogIn'))
    
    finally:
        cursor.close()
        dataBase.close()

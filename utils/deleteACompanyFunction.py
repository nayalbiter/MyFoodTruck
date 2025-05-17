from flask import redirect, request, url_for
from flask_login import current_user, logout_user
from utils.databaseInfo import connectToDatabase
import mysql.connector

def deleteCompany():
    
    company_id = request.form.get('company_id')
    print(f"this is the company_id : {company_id}")
    
    if not company_id or int(company_id) != current_user.id:
        print("Something is wrong. You are not allowed to delete this account")
        logout_user()
        return redirect(url_for("index"))
    
    deleteFoodCompanyQuery = "delete from food_companies where company_id = %s "
    
    try:
        dataBase = connectToDatabase()
        cursor = dataBase.cursor(dictionary=True)
        cursor.execute(deleteFoodCompanyQuery, (current_user.id,))
        dataBase.commit()
        logout_user()
        print("Your company and its food trucks have been deleted successfully")
        return redirect(url_for('index'))
        
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        print(f"An error occurred while deleting this food company: {err}")
        return redirect(url_for('go2CompanyMainPageAfterLogIn'))
    
    finally:
        cursor.close()
        dataBase.close()

from flask import render_template, request
from utils.databaseInfo import connectToDatabase
import mysql.connector

def getCompanyIdForFoodTRuckForm():
    company_id = request.args.get('company_id')

    if not company_id:
        return "This company does not exist", 400

    try:
        db = connectToDatabase()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM food_companies WHERE company_id = %s", (company_id,))
        company = cursor.fetchone()
        
    except mysql.connector.Error as err:
        return f"Database error: {err}", 500
    
    finally:
        cursor.close()
        db.close()

    if not company:
        return "Company not found", 404

    return render_template("addNewFoodTruckForm.html", company=company)

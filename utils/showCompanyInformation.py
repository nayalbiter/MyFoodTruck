from flask import render_template
from utils.databaseInfo import connectToDatabase
import mysql.connector

def showCompanyInfo(company_id):
    try:
        db = connectToDatabase()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            select company_name, food_description, business_website, email 
            from food_companies 
            where company_Id = %s
        """, (company_id,))
        company = cursor.fetchone()

        if not company:
            return "Company not found", 404 # to do: create the 404 page not found
        
        cursor.execute("""
            select food_truck_name
            from food_trucks 
            where company_Id = %s
        """, (company_id,))
        food_trucks = cursor.fetchall()
        if not food_trucks:
            food_trucks = []

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return f"Database error: {err}", 500

    finally:
        cursor.close()
        db.close()

    return render_template("foodCompanyPage.html", company=company, food_trucks=food_trucks)
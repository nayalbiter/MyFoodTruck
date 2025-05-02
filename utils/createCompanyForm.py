from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash
from utils.databaseInfo import connectToDatabase
import mysql.connector

def createCompany():
    company_name = request.form['company']
    food_description = request.form['foodTruckDescription']
    business_website = request.form['foodTruckWebsite']
    company_email = request.form['companyEmail']
    password = request.form['companyPassword']
    secure_password = generate_password_hash(password)

    insertCompany_query = """
    INSERT INTO food_companies (company_name, food_description, business_website, email, password)
    VALUES (%s, %s, %s, %s, %s)
    """
    try:
        foodTruckDb = connectToDatabase()
        cursor = foodTruckDb.cursor(dictionary=True)
        cursor.execute(insertCompany_query, (company_name, food_description, business_website, company_email,secure_password))
        foodTruckDb.commit()

        #show the information of the company in the food Company main page
        cursor.execute("""
            SELECT company_name, food_description, business_website, email 
            FROM food_companies 
            WHERE company_Id = LAST_INSERT_ID()
        """)
        company = cursor.fetchone()
        
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return f"An error happened while processing your request: {err}", 500  #server error
    
    finally:
        cursor.close()
        foodTruckDb.close()
        
    print(f"Company details fetched: {company}")
    return render_template("foodCompanyPage.html", company=company)
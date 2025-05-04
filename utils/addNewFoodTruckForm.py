from flask import Flask, redirect, render_template, request, url_for
from utils.databaseInfo import connectToDatabase
import mysql.connector

def addNewFoodTruck():
    food_truck_name = request.form['foodTruckName']
    food_truck_location = request.form['address']
    phone_number = request.form['phone']
    business_hours = request.form['hours']
    companyID = request.form['company_Id']
    
    insertFoodTruckQuery = """
    INSERT INTO food_trucks (food_truck_name, food_truck_location, phone_number, business_hours, company_id )
    VALUES (%s, %s, %s, %s, %s)
    """
    try:
        foodTruckDb = connectToDatabase()
        cursor = foodTruckDb.cursor(dictionary=True)
        cursor.execute(insertFoodTruckQuery, (food_truck_name, food_truck_location, phone_number, business_hours, companyID))
        foodTruckDb.commit()

        return redirect(url_for('showCompanyPage', companyID=companyID))
    
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return f"An error happened while processing your request: {err}", 500  #server error
    
    finally:
        cursor.close()
        foodTruckDb.close()
        
    return render_template("foodCompanyPage.html", company=company, food_trucks=food_trucks)

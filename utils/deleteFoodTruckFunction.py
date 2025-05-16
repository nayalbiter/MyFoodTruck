from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user
from utils.databaseInfo import connectToDatabase
from utils.getFoodTrucksListPerCompany import getFTList
import mysql.connector

def deleteFoodTruck():
    
    food_truck_id = request.form.get('food_truck_id')
    print(f"this is the food truck id : {food_truck_id}")
    
    if not food_truck_id:
        flash(f"this food truck does not exist", Warning)
        return redirect(url_for("go2CompanyMainPageAfterLogIn"))
    
    company_id = current_user.id
    
    deleteFoodTruckQuery = "delete from food_trucks where food_truck_id = %s and company_id = %s "
    
    try:
        foodTruckDb = connectToDatabase()
        cursor = foodTruckDb.cursor(dictionary=True)
        cursor.execute(deleteFoodTruckQuery, (food_truck_id, company_id))
        foodTruckDb.commit()
    
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        flash(f"An error occurred while deleting this food truck: {err}", "danger")
    
    finally:
        cursor.close()
        foodTruckDb.close()
            
    updated_food_trucks_list = getFTList(company_id)
    
    return render_template("foodCompanyPage.html", company = current_user, food_trucks = updated_food_trucks_list )
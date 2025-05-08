from flask import Flask, redirect, render_template, request, url_for
from utils.databaseInfo import connectToDatabase
import mysql.connector

def getFoodTrucksFromDB():
    try:
        foodTruckDb = connectToDatabase()
        cursor = foodTruckDb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM food_trucks")
        food_trucks = cursor.fetchall()
        
        # for food_truck in food_trucks:
        #     print(food_truck)
        
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return f"An error happened while processing your request: {err}"
    
    finally:
        cursor.close()
        foodTruckDb.close()
    
    return food_trucks


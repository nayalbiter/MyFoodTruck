from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash
import mysql.connector

app = Flask(__name__)

#connect to database locally CHECK
def connectToDatabase():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Food_Trucks_Database"
    )

# Home page
@app.route('/')
def index():
    return render_template("index.html")

# Register Food Truck company
@app.route('/registerFoodCompanyPage')
def go2RegisterCompany():
    return render_template("registerFoodTruckCompany.html")

# create company's form
@app.route('/createCompany', methods=['POST'])
def createCompanyForm():
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
        if not company:
            raise ValueError("No company data found after insertion.")
        
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return f"An error occurred while processing your request: {err}", 500
    
    finally:
        cursor.close()
        foodTruckDb.close()
        
    print(f"Company details fetched: {company}")
    return render_template("foodCompanyPage.html", company=company)

if __name__ == '__main__':
    app.run(debug=True)

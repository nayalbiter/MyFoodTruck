from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


#connection to dBase locally --CHECK THIS!!!
foodTrucks_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Food_Trucks_Database"
)

cursor = foodTrucks_db.cursor()

#food truck owners set up
@app.route('/registerFoodCompanyPage')
def go2RegisterCompany():
    return render_template("registerFoodTruckCompany.html")


#register a company
@app.route('/createCompany', methods=['POST'])
def createCompanyForm():
    company_name = request.form['company']
    food_description = request.form['foodTruckDescription']
    business_website =  request.form['foodTruckWebsite']
    company_email = request.form['companyEmail']
    password = request.form['companyPassword']
    
    secure_password = generate_password_hash(password)
    
    query = """
    INSERT INTO food_companies (company_name, food_description, business_website, email, password)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    #todo: include a try/except for error handling, just in case...CHEck
    cursor.execute(query, (company_name, food_description, business_website, company_email, secure_password))

    foodTrucks_db.commit()

    print ("Company profile created successfully!")
    return render_template("foodCompanyPage.html")
    

if __name__ == '__main__':
    app.run(debug=True)
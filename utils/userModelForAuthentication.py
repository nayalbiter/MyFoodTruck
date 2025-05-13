from flask_login import UserMixin
from werkzeug.security import check_password_hash
from utils.databaseInfo import connectToDatabase

class User(UserMixin):
    def __init__(self, company_id, company_name, company_email, password):
        self.id = company_id
        self.company_name = company_name
        self.company_email = company_email
        self.password = password

    @staticmethod
    def getCompanyEmail(company_email):
        dbConnection = connectToDatabase()
        cursor = dbConnection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM food_companies WHERE email = %s", (company_email,))
        company = cursor.fetchone()
        dbConnection.close()

        if company:
            return User(company['company_id'], company['company_name'], company['email'], company['password'])
        return None

    @staticmethod
    def get_by_id(company_id):
        dbConnection = connectToDatabase()
        cursor = dbConnection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM food_companies WHERE company_id = %s", (company_id,))
        company = cursor.fetchone()
        dbConnection.close()

        if company:
            return User(company['company_id'], company['company_name'], company['email'], company['password'])
        return None

    def checkPassword(self, userPassword):
        return check_password_hash(self.password, userPassword)

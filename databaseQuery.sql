create database Food_Trucks_Database;
use Food_Trucks_Database;

/* company table */   		/* to do: add the unique attribute to the company name*/
create table food_companies (
	company_Id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	company_name VARCHAR(255) NOT NULL,     
	food_description TEXT NOT NULL,
	business_website VARCHAR(255),
	email VARCHAR(255) NOT NULL, 
	password VARCHAR(255) NOT NULL
);
/*food trucks table */
CREATE TABLE food_trucks (
    food_truck_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    food_truck_name VARCHAR(255) NOT NULL,
    full_address TEXT NOT NULL,
    phone_number VARCHAR(20),
    business_hours VARCHAR(100),
    company_Id INT NOT NULL,
    FOREIGN KEY (company_Id) REFERENCES food_companies(company_Id)
);

select * from food_companies;
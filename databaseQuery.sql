DROP DATABASE IF EXISTS Food_Trucks_Database;
create database Food_Trucks_Database;
use Food_Trucks_Database;
/* company table */ 
create table food_companies (
	company_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	company_name VARCHAR(255) NOT NULL UNIQUE,     
	food_description TEXT NOT NULL,
	business_website VARCHAR(255),
	email VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL
);
/*food trucks table */
CREATE TABLE food_trucks (
    food_truck_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    food_truck_name VARCHAR(255) NOT NULL,
    full_address TEXT NOT NULL,
    phone_number VARCHAR(20),
    business_hours VARCHAR(100),
    company_id INT NOT NULL,
    FOREIGN KEY (company_id) REFERENCES food_companies(company_id) ON DELETE CASCADE
);

select * from food_companies;
select * from food_trucks;




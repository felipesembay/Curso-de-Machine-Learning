#MYSQL
CREATE TABLE bank_model (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Age INT,
    `Married/Single` INT,
    Experience INT,
    Profession INT,
    CURRENT_JOB_YRS INT,
    House_Ownership INT,
    Car_Ownership INT,
    CURRENT_HOUSE_YRS INT,
    income FLOAT,
    City VARCHAR(255),
    State VARCHAR(255),
    Prediction INT,
    Prediction_Probability FLOAT
);


#POSTGRES
CREATE TABLE bank_model (
    id SERIAL PRIMARY KEY,
    "Name" VARCHAR(255),
    "Age" INT,
    "Married/Single" INT,
    "Experience" INT,
    "Profession" INT,
    "CURRENT_JOB_YRS" INT,
    "House_Ownership" INT,
    "Car_Ownership" INT,
    "CURRENT_HOUSE_YRS" INT,
    income FLOAT,
    "City" VARCHAR(255),
    "State" VARCHAR(255),
    "Prediction" INT,
    "Prediction_Probability" FLOAT
);

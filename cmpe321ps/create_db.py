import mysql.connector
import environ
from hashlib import sha256

env = environ.Env()
environ.Env.read_env()

connection = mysql.connector.connect(
  host=env("MYSQL_HOST"),
  user=env("MYSQL_USER"),
  password=env("MYSQL_PASSWORD"),
  database=env("MYSQL_DATABASE"),
  auth_plugin='mysql_native_password'
)
cursor= connection.cursor()
#Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Camera(
	cameraID int UNIQUE,
	PRIMARY KEY (cameraID)
);""")

cursor= connection.cursor()
#Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Product(
	cameraID int UNIQUE,
	vehicleID varchar(255),
	productName varchar(255) UNIQUE,
 	count int,
	start_date TIMESTAMP,
	end_date TIMESTAMP,
	PRIMARY KEY (productName)
);""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Manager(
	username varchar(255),
	password varchar(255),
    PRIMARY KEY(username)
);""")

connection.commit()

password = sha256("232206".encode("utf-8")).hexdigest()

cursor.execute(f"""
INSERT INTO Manager VALUES ('Takkin', '{password}')
""")

connection.commit()

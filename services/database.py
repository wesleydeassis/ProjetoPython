import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="wesley@adm123",
    database="tcc_outlier"
)

mycursor = mydb.cursor()

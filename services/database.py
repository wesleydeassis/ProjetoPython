import pymysql

cnx = pymysql.connect(host="localhost", database="tcc_outlier",
                      user="root", password="wesley@adm123")  # Conexão
cursor = cnx.cursor()  # Executar as querys

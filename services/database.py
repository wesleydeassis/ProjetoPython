import pymysql

cnx = pymysql.connect(host="localhost", port=8501, database="tcc_outlier",
                      user="root", password="wesley@adm123")  # Conexão
cursor = cnx.cursor()  # Executar as querys

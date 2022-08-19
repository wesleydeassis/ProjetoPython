import services.database as db


def createUser(usuario):
    db.cursor.execute("INSERT INTO tab_users (nome, email, departamento, senha)\
    values (%s, %s, %s, %s)")
    db.cnx.commit()
   # return "sucesso"

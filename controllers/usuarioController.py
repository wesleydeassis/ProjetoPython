import services.database as db


def createUser(usuario):
    db.cursor.execute(sql, valores)

    sql = ("INSERT INTO tab_users (nome, email, departamento, senha)\
    values (%s, %s,%s, %s);")
    valores = (usuario.nome, usuario.email,
               usuario.departamento, usuario.senha)

    db.cnx.commit()
   # return "sucesso"

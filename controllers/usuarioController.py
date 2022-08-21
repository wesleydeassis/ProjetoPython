import services.database as db


def createUser(usuario):
    sql = "INSERT INTO tab_users (nome, email, departamento, senha) VALUES (%s, %s,%s, %s)"
    val = (usuario.nome, usuario.email, usuario.departamento, usuario.senha)
    db.mycursor.execute(sql, val)

    db.mydb.commit()
   # return "sucesso"

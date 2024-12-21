from log import log

def insert_user(nome, idade):
    conection = log()

    if conection:
        try:

            cursor = conection.cursor()
            sql = "INSERT INTO usuarios(nome, idade) VALUES (%s, %s)"

            cursor.execute(sql, (nome, idade))
            conection.commit()

            print(" --- usuário inserido com sucesso --- \n")
        except Exception as e:
            print(f" -- Erro ao inserir usuário: \n {e} \n")
        finally:
            cursor.close()
            conection.close()

def search():

    conection = log()

    if conection:

        try:
            cursor = conection.cursor()

            sql = "SELECT * FROM usuarios"

            cursor.execute(sql)
            #conection.commit()

            rows = cursor.fetchall()

            print(f" \n {rows} \n")

        except Exception as e:
            print(f"\n Erro ao buscar \nErro: {e} ")
        finally:
            cursor.close()
            conection.close()

search()
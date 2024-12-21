from log import log


# function for insert data in database
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

# function for search all the user in database
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


# function for make search smart in database
def search_smart(name):

    conection = log()

    if conection:

        try:

            cursor = conection.cursor()

            if nome:
                sql = "SELECT nome FROM usuarios WHERE nome LIKE %s"

                cursor.execute(sql, ('%' +nome+ '%',))

                rows = cursor.fetchall()

                if rows:
                    print(f"\n {rows} \n")
                else:
                    print("\n -- Dado não encontrado -- \n")


            else:
                print(" Necessario nome")
        except Exception as e:
            print(f"\n Erro ao fazer a busca: \n{e}\n ")
        finally:
            cursor.close()
            conection.close()

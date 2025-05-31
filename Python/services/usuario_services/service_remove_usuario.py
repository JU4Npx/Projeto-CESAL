from config.conexao import conexaoBD


def remover_usuario():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuario ORDER BY ID_usuario")
    dados_usuarios = cursor.fetchall()
    print(f"-" * 30)
    print("       LISTA DE USUARIOS        ")
    print(f"-" * 30)
    print("")
    for dado in dados_usuarios:
        print(f"ID: {dado[0]}  Nome: {dado[1]}  E-mail: {dado[2]}  Cargo: {dado[4]}")
        print(f"-" * 120)
        while True:
            try:
                print("")
                ID_busca = int(input("Digite o ID do usuário que deseja remover (ou 0 para voltar): "))
                if ID_busca == 0:
                    break
                elif ID_busca == 1:
                    print("Não é possível remover o usuário de ID 1, pois é o administrador do sistema.")
                else:
                    cursor.execute("DELETE FROM usuario WHERE ID_usuario = %s", (ID_busca,))
                    con.commit()
                    print(f"Usuário de ID {ID_busca}, foi removido com sucesso!")
                    break
            except Exception as e:
                print(f"Erro ao tentar remover usuario")
                print(f"Erro {e} ")
            finally:
                cursor.close()
                con.close()
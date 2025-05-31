from config.conexao import conexaoBD


def remover_professor():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM professor ORDER BY ID_professor")
    dados_professores = cursor.fetchall()
    print(f"-" * 30)
    print("     LISTA DE PROFESSORES       ")
    print(f"-" * 30)
    print("")
    for dado in dados_professores:
        print(f"ID: {dado[0]}  Nome: {dado[1]}  Idade: {dado[2]}  E-mail: {dado[3]}  Telefone: {dado[4]}  Formação: {dado[5]}")
        print(f"-" * 120)
    while True:
        try:
            print("")
            ID_busca = int(input("Digite o ID do professor que deseja remover (ou 0 para voltar): "))
            if ID_busca == 0:
                break
            else:
                cursor.execute("DELETE FROM professor WHERE ID_professor = %s", (ID_busca,))
                con.commit()
                print(f"Professor de ID {ID_busca}, foi removido com sucesso!")
                break
        except Exception as e:
            print(f"Erro ao tentar remover professor")
            print(f"Erro {e} ")
        finally:
            cursor.close()
            con.close()
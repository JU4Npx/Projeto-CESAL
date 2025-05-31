from config.conexao import conexaoBD


def remover_aluno():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM aluno ORDER BY ID_aluno")
    dados_alunos = cursor.fetchall()
    print(f"-" * 30)
    print("        LISTA DE ALUNOS        ")
    print(f"-" * 30)
    print("")
    for dado in dados_alunos:
        print(f"ID: {dado[0]}  Nome: {dado[1]}  Idade: {dado[2]}  E-mail: {dado[3]}  Endereço: {dado[4]}  Telefone: {dado[5]}")
        print(f"-" * 120)
    while True:
        try:
            print("")
            ID_busca = int(input("Digite o ID do aluno que deseja remover (ou 0 para voltar): "))
            if ID_busca == 0:
                break
            else:
                cursor.execute("DELETE FROM aluno WHERE ID_aluno = %s", (ID_busca,))
                con.commit()
                print(f"Aluno de ID {ID_busca}, foi removido com sucesso!")
                break
        except Exception as e:
            print(f"Erro ao tentar remover o aluno")
            print(f"Erro {e} ")
        finally:
            cursor.close()
            con.close()
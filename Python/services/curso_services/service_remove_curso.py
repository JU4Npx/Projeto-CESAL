from config.conexao import conexaoBD


def remover_curso():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM curso ORDER BY ID_curso")
    dados_cursos = cursor.fetchall()
    print(f"-" * 30)
    print("        LISTA DE CURSOS        ")
    print(f"-" * 30)
    print("")
    for dado in dados_cursos:
        print(f"ID: {dado[0]}  Nome: {dado[1]}  Descrição: {dado[2]}  Valor: {dado[3]}  Carga horária: {dado[4]}  Numero de vagas: {dado[5]}")
        print(f"-" * 120)
    while True:
        try:
            print("")
            ID_busca = int(input("Digite o ID do curso que deseja remover (ou 0 para voltar): "))
            if ID_busca == 0:
                break
            else:
                cursor.execute("DELETE FROM curso WHERE ID_curso = %s", (ID_busca,))
                con.commit()
                print(f"Curso de ID {ID_busca}, foi removido com sucesso!")
                input("Pressione ENTER para continuar...")
                break
        except Exception as e:
            print(f"Erro ao tentar remover curso")
            print(f"Erro {e} ")
        finally:
            cursor.close()
            con.close()
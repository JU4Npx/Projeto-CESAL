from config.conexao import conexaoBD
from services.tools.tools import validacao_email

def lista_disciplina():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM disciplina ORDER BY ID_disciplina")
    dados_disciplina = cursor.fetchall()
    print(f"-" * 30)
    print("     LISTA DE DISCIPLINAS       ")
    print(f"-" * 30)
    print("")
    for dado in dados_disciplina:
        print(f"ID: {dado[0]}  Nome: {dado[1]}  Descrição: {dado[2]}")
        print(f"-" * 120)
    input("Pressione ENTER para voltar ao menu...")
    cursor.close()
    con.close()

def editar_disciplina():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM disciplina ORDER BY ID_disciplina")
    dados_disciplina = cursor.fetchall()
    if not dados_disciplina:
        print("Nenhuma disciplina encontrada.")
        input("Pressione ENTER para voltar ao menu...")
        cursor.close()
        con.close()
        return
    while True:
        print(f"-" * 30)
        print("     LISTA DE DISCIPLINAS       ")
        print(f"-" * 30)
        print("")
        for dado in dados_disciplina:
            print(f"ID: {dado[0]}  Nome: {dado[1]}  Descrição: {dado[2]}")
            print(f"-" * 120)
            try:
                ID_disciplina = int(input("Digite o ID da disciplina que deseja editar: "))
                cursor.execute("SELECT * FROM disciplina WHERE ID_disciplina = %s", (ID_disciplina,))
                disciplina = cursor.fetchone()
                if disciplina is None:
                    print("Disciplina não encontrada.")
                    return
                else:
                    print(f"Você selecionou a disciplina: {disciplina[0]} - {disciplina[1]}")
                    print("\n 1 - Editar disciplina")
                    print("\n 2 - sair")
                    opcao = int(input("Digite a opção desejada: "))
                    try:
                        if opcao == 1:    
                            novo_nome = input("Digite o novo nome da disciplina: ")
                            nova_descricao = input("Digite a nova descrição da disciplina: ")
                            cursor.execute("UPDATE disciplina SET nome_disciplina = %s, descricao_disciplina = %s WHERE ID_disciplina = %s",(novo_nome, nova_descricao, ID_disciplina))
                            con.commit()
                            print(f"Disciplina com ID {ID_disciplina} editada com sucesso!")
                            input("Pressione ENTER para continuar...")
                        elif opcao == 2:
                            break
                    except ValueError:
                        print("Opção inválida. Tente novamente.")
                        continue
            except ValueError:
                print("Disciplina não encontrada ou entrada inválida. Tente novamente.")
            finally:
                cursor.close()
                con.close()
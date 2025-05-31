
from config.conexao import conexaoBD
import time
import os

def lista_curso():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM curso ORDER BY ID_curso")
    dados_curso = cursor.fetchall()
    print(f"-" * 30)
    print("        LISTA DE CURSOS        ")
    print(f"-" * 30)
    print("")
    for dado in dados_curso:
        print(f"ID: {dado[0]}  Nome: {dado[1]}  Descrição: {dado[2]}  Valor: R${dado[3]}  Carga Horária: {dado[4]}  Vagas: {dado[5]}")
        print(f"-" * 120)
    input("Pressione ENTER para voltar ao menu...")
    cursor.close()
    con.close()

def editar_lista_curso():
    while True:
        con = conexaoBD()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM curso ORDER BY ID_curso")
        dados_curso = cursor.fetchall()
        print(f"-" * 30)
        print("        LISTA DE CURSOS        ")
        print(f"-" * 30)
        print("")
        for dado in dados_curso:
            print(f"ID: {dado[0]}  Nome: {dado[1]}  Descrição: {dado[2]}  Valor: {dado[3]}  Carga Horária: {dado[4]}  Vagas: {dado[5]}")
            print(f"-" * 120)
        try:
            print("")
            ID_busca = (input("Digite o ID do curso que deseja editar, ou 0 para voltar: "))
            if ID_busca == '0':
                print("Voltando...")
                time.sleep(1.5)
                os.system('cls')
                break
            else:
                cursor.execute("SELECT * FROM curso WHERE ID_curso = %s", (ID_busca,))
                curso = cursor.fetchone()
                if curso is None:
                    print("ID não encontrado.")
                    return
                print("")
                print(f"Aluno selecionado: {curso[1]} (ID {curso[0]})")
                print("O que deseja editar?")
                print("1 - Nome")
                print("2 - Descrição")
                print("3 - Valor")
                print("4 - Carga Horária")
                print("5 - Vagas")
                print("0 - Voltar")
                try:
                    opcao = int(input("Escolha a opção (0-5): "))

                    if opcao == 1:
                        novo_nome = input("Digite o novo nome: ")
                        cursor.execute("UPDATE curso SET nome_curso = %s WHERE ID_curso = %s", (novo_nome, ID_busca))
                        con.commit()
                        print("Nome editado com sucesso!")
                        time.sleep(1.5)
                        os.system('cls')
                    elif opcao == 2:
                        nova_descricao = input("Digite a nova descrição: ")
                        cursor.execute("UPDATE curso SET descricao = %s WHERE ID_curso = %s", (nova_descricao, ID_busca))
                        con.commit()
                        print("Descrição editada com sucesso!")
                        time.sleep(1.5)
                        os.system('cls')
                    elif opcao == 3:
                        while True:
                            try:
                                novo_valor = float(input("Digite o novo valor: R$"))
                                if novo_valor <= 0:
                                    print("Número inválido, o valor não pode ser menor ou igual a zero.")
                                else:
                                    cursor.execute("UPDATE curso SET valor_curso = %s WHERE ID_curso = %s", (novo_valor, ID_busca))
                                    con.commit()
                                    print("Valor editado com sucesso!")
                                    time.sleep(1.5)
                                    os.system('cls')
                                    break
                            except ValueError:
                                print("Entrada inválida. Digite um número válido.")
                    elif opcao == 4:
                        while True:
                            try:
                                nova_carga_horaria = int(input("Digite a nova carga horária: "))
                                if nova_carga_horaria <= 0:
                                    print("Valor inválido, a carga horária não pode ser menor, ou igual a zero")
                                else:
                                    cursor.execute("UPDATE curso SET carga_horaria = %s WHERE ID_curso = %s", (nova_carga_horaria, ID_busca))
                                    con.commit()
                                    print("Carga horária editada com sucesso!")
                                    time.sleep(1.5)
                                    os.system('cls')
                                    break
                            except ValueError:
                                print("Entrada inválida. Digite um número válido.")
                    elif opcao == 5:
                        while True:
                            try:
                                novo_numero_vagas = int(input("Digite o novo novo número de vagas: "))
                                if novo_numero_vagas < 0:
                                    print("Valor inválido, a carga horária não pode ser menor que zero")
                                else:
                                    cursor.execute("UPDATE curso SET numero_vagas = %s WHERE ID_curso = %s", (novo_numero_vagas , ID_busca))
                                    con.commit()
                                    print("Número de vagas alterado com sucesso!")
                                    time.sleep(1.5)
                                    os.system('cls')
                                    break
                            except ValueError:
                                print("Entrada inválida. Digite um número válido.")
                    elif opcao == 0:
                        print("Voltando...")
                        time.sleep(1.5)
                        os.system('cls')
                        break
                except ValueError:
                    print("Opção inválida.")
                    return
        except Exception as e:
            print("Erro ao buscar curso")
            print(f"Erro {e}")
    cursor.close()
    con.close()                                

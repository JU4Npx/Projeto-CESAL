from config.conexao import conexaoBD
from services.tools.tools import validacao_email
import time
import os

def lista_professor():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM professor")
    dados_professor = cursor.fetchall()
    print(f"-" * 30)
    print("     LISTA DE PROFESSORES       ")
    print(f"-" * 30)
    print("")
    for dado in dados_professor:
        print(f"ID: {dado[0]}  Nome: {dado[1]}  Idade: {dado[2]}  E-mail: {dado[3]}  Telefone: {dado[4]}  Formação: {dado[5]}")
        print(f"-" * 120)
    cursor.close()
    con.close()

def editar_lista_professor():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM professor")
    dados_professor = cursor.fetchall()
    print(f"-" * 30)
    print("     LISTA DE PROFESSORES       ")
    print(f"-" * 30)
    print("")
    for dado in dados_professor:
        print(f"ID: {dado[0]}  Nome: {dado[1]}  Idade: {dado[2]}  E-mail: {dado[3]}  Telefone: {dado[4]}  Formação: {dado[5]}")
        print(f"-" * 120)
    while True:
        try:
            print("")
            ID_busca = (input("Digite o ID do professor que deseja editar, ou 0 para voltar: "))
            if ID_busca == '0':
                print("Voltando...")
                time.sleep(1.5)
                os.system('cls')
                break
            else:
                cursor.execute("SELECT * FROM professor WHERE ID_professor = %s", (ID_busca,))
                professor = cursor.fetchone()
                if professor is None:
                    print("ID não encontrado.")
                    return
                print("")
                print(f"Aluno selecionado: {professor[1]} (ID {professor[0]})")
                print("O que deseja editar?")
                print("1 - Nome")
                print("2 - Idade")
                print("3 - E-mail")
                print("4 - Telefone")
                print("5 - Formação")
                print("0 - Voltar")
                
                try:
                    opcao = int(input("Escolha a opção (0-5): "))

                    if opcao == 1:
                        novo_nome = input("Digite o novo nome: ")
                        cursor.execute("UPDATE professor SET nome_professor = %s WHERE ID_professor = %s", (novo_nome, ID_busca))
                        con.commit()
                        print("Nome editado com sucesso!")
                        time.sleep(1.5)
                        os.system('cls')
                    if opcao == 2:
                        while True:
                            try:
                                nova_idade = int(input("Digite a nova idade: "))
                                if nova_idade <18:
                                    print("Idade inválida, o aluno não pode ter menos que dezoito anos.")
                                else:
                                    cursor.execute("UPDATE professor SET idade_professor = %s WHERE ID_professor = %s", (nova_idade, ID_busca))
                                    con.commit()
                                    print("Idade editada com sucesso!")
                                    time.sleep(1.5)
                                    os.system('cls')
                                    break
                            except ValueError:
                                print("Entrada inválida. Digite um número válido.")
                    if opcao == 3:
                         while True:
                            novo_email = input("Digite o novo e-mail: ")
                            if not validacao_email(novo_email):
                                print("Email inválido, tente novamente.")
                            else:
                                cursor.execute("UPDATE professor SET email_professor = %s WHERE ID_professor = %s", (novo_email, ID_busca))
                                con.commit()
                                print("E-mail editado com sucesso!")
                                time.sleep(1.5)
                                os.system('cls')
                                break
                    if opcao == 4:
                        while True:
                             try:
                                novo_telefone = input("Por favor, digite o telefone do aluno(com '55' + DDD e os números sem espaço): ")
                                if len(novo_telefone) < 12:
                                    print("Telefone inválido. Deve conter pelo menos 12 dígitos.")
                                else:
                                    cursor.execute("UPDATE professor SET telefone_professor = %s WHERE ID_professor = %s", (novo_telefone, ID_busca))
                                    con.commit()
                                    print("Telefone editado com sucesso!")
                                    time.sleep(1.5)
                                    os.system('cls')
                                    break
                             except ValueError:
                                print("Entrada inválida. Digite um número válido.")
                    if opcao == 5:
                        nova_formacao = input("Digite a formação: ")
                        cursor.execute("UPDATE professor SET formacao = %s WHERE ID_professor = %s", (nova_formacao, ID_busca))
                        con.commit()
                        print("Formação alterada com sucesso!")
                        time.sleep(1.5)
                        os.system('cls')
                        break
                except ValueError:
                    print("Opção inválida.")
                    return
        except Exception as e:
            print("Erro ao buscar professor")
            print(f"Erro {e}")
    cursor.close()
    con.close()
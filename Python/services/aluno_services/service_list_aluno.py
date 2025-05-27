from config.conexao import conexaoBD
from services.tools import validacao_email
import time
import os

def lista_aluno():
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
    cursor.close()
    con.close()


def editar_lista_aluno():
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
            ID_busca = (input("Digite o ID do aluno(a) que deseja editar, ou 0 para voltar: "))
            if ID_busca == '0':
                print("Voltando...")
                time.sleep(1.5)
                os.system('cls')
                break
            else:
                cursor.execute("SELECT * FROM aluno WHERE ID_aluno = %s", (ID_busca,))
                aluno = cursor.fetchone()
                if aluno is None:
                    print("ID não encontrado.")
                    return
                print("")
                print(f"Aluno selecionado: {aluno[1]} (ID {aluno[0]})")
                print("O que deseja editar?")
                print("1 - Nome")
                print("2 - Idade")
                print("3 - E-mail")
                print("4 - Endereço")
                print("5 - Telefone")
                print("0 - Voltar")
                try:
                    opcao = int(input("Escolha a opção (0-5): "))
                    if opcao == 1:
                        novo_nome = input("Digite o novo nome: ")
                        cursor.execute("UPDATE aluno SET nome_aluno = %s WHERE ID_aluno = %s", (novo_nome, ID_busca))
                        con.commit()
                        print("Nome editado com sucesso!")
                        time.sleep(1.5)
                        os.system('cls')
                    elif opcao == 2:
                        while True:
                            try:
                                nova_idade = int(input("Digite a nova idade: "))
                                if nova_idade <16:
                                    print("Idade inválida, o aluno não pode ter menos que dezesseis anos.")
                                else:
                                    cursor.execute("UPDATE aluno SET idade_aluno = %s WHERE ID_aluno = %s", (nova_idade, ID_busca))
                                    con.commit()
                                    print("Idade editada com sucesso!")
                                    time.sleep(1.5)
                                    os.system('cls')
                                    break
                            except ValueError:
                                print("Entrada inválida. Digite um número válido.")
                    elif opcao == 3:
                        while True:
                            novo_email = input("Digite o novo e-mail: ")
                            if not validacao_email(novo_email):
                                print("Email inválido, tente novamente.")
                            else:
                                cursor.execute("UPDATE aluno SET email_aluno = %s WHERE ID_aluno = %s", (novo_email, ID_busca))
                                con.commit()
                                print("E-mail editado com sucesso!")
                                time.sleep(1.5)
                                os.system('cls')
                                break
                    elif opcao == 4:
                        novo_endereco = input("Digite o novo endereço: ")
                        cursor.execute("UPDATE aluno SET endereco_aluno = %s WHERE ID_aluno = %s", (novo_endereco, ID_busca))
                        con.commit()
                        print("Endereço editado com sucesso!")
                        time.sleep(1.5)
                        os.system('cls')
                    elif opcao == 5:
                        while True:
                             try:
                                novo_telefone = input("Por favor, digite o telefone do aluno(com '55' + DDD e os números sem espaço): ")
                                if len(novo_telefone) < 12:
                                    print("Telefone inválido. Deve conter pelo menos 12 dígitos.")
                                else:
                                    cursor.execute("UPDATE aluno SET telefone_aluno = %s WHERE ID_aluno = %s", (novo_telefone, ID_busca))
                                    con.commit()
                                    print("Telefone editado com sucesso!")
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
            print("Erro ao buscar Aluno")
            print(f"Erro {e}")
    cursor.close()
    con.close()

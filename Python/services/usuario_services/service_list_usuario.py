from config.conexao import conexaoBD
from tools.tools import validacao_email
import base64
import bcrypt    
import time
import os

def lista_usuario():
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
    cursor.close()
    con.close()

def editar_lista_usuario():
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
            ID_busca = (input("Digite o ID do usuario que deseja editar, ou 0 para voltar: "))
            if ID_busca == '0':
                print("Voltando...")
                time.sleep(1.5)
                os.system('cls')
                break
            else:
                cursor.execute("SELECT * FROM usuario WHERE ID_usuario = %s", (ID_busca,))
                usuario = cursor.fetchone()
                if usuario is None:
                    print("ID não encontrado.")
                    return
                else:
                    print("")
                print(f"Aluno selecionado: {usuario[1]} (ID {usuario[0]})")
                print("O que deseja editar?")
                print("1 - Nome")
                print("2 - E-mail")
                print("3 - Senha")
                print("4 - Cargo")
                print("0 - Voltar")
                
                try:
                    opcao = int(input("Escolha a opção (0-5): "))
                    
                    if opcao == 1:
                        novo_nome = input("Digite o novo nome: ")
                        cursor.execute("UPDATE usuario SET nome_usuario = %s WHERE ID_usuario = %s", (novo_nome, ID_busca))
                        con.commit()
                        print("Nome alterado com sucesso!")
                    if opcao == 2:
                        while True:
                            novo_email  = input("Por favor, digite o novo E-mail: ")
                            if not validacao_email(novo_email):
                                print("Email inválido, tente novamente.")
                            else:
                                cursor.execute("UPDATE usuario SET email_usuario = %s WHERE ID_usuario = %s", (novo_email, ID_busca))
                                con.commit()
                                print("Email alterado com sucesso!")
                                break
                    if opcao == 3:
                        while True:
                            nova_senha = input("Digite a nova senha (com no minimo 8 caracteres): ")
                            if len(nova_senha) < 8:
                                print("Digite com no minimo 8 caracteres!")
                            else:
                                senha_bytes = nova_senha.encode('utf-8')
                                senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
                                senha_hash_str = base64.b64encode(senha_hash).decode('utf-8')
                                cursor.execute("UPDATE usuario SET senha_hash = %s WHERE ID_usuario = %s", (senha_hash_str, ID_busca))
                                con.commit()
                                print("senha modificada com sucesso!")
                                break
                    if opcao == 4:
                        cursor.execute("SELECT nome_usuario FROM usuario WHERE ID_usuario = %s", (ID_busca,))
                        nome = cursor.fetchone()
                        print(f"Deseja modificar o cargo de {nome}? ")
                        print("\n 1 - sim")
                        print("\n 2 - não")
                        escolha = int(input("\nOpção: "))
                        try:
                            if escolha == 1:
                                cursor.execute("SELECT role FROM usuario WHERE ID_usuario = %s", (ID_busca,))
                                cargo = cursor.fetchone()
                                if cargo == 'admin':
                                    print(f"Deseja mudar {nome} para usuario? ")
                                    print("\n 1 - sim")
                                    print("\n 2 - não")
                                    escolha_adm = int(input("\nOpção: "))
                                    try:
                                        if escolha_adm == 1:
                                            cargo_adm = 'user'
                                            cursor.execute("UPDATE usuario SET role = %s WHERE ID_usuario = %s", (cargo_adm, ID_busca))
                                            con.commit()
                                            print("Cargo alterado com sucesso!")
                                        else:
                                            break
                                    except ValueError:
                                        print("escolha uma opção válida!")
                                elif cargo == 'user':
                                    print(f"Deseja mudar {nome} para admin? ")
                                    print("\n 1 - sim")
                                    print("\n 2 - não")
                                    escolha_usuario = int(input("\nOpção: "))
                                    try:
                                        if escolha_usuario == 1:
                                            cargo_usuario = 'admin'
                                            cursor.execute("UPDATE usuario SET role = %s WHERE ID_usuario = %s", (cargo_usuario, ID_busca))
                                            con.commit()
                                            print("Cargo alterado com sucesso!")
                                        elif escolha_usuario == 2:
                                            break
                                    except ValueError:
                                        print("escolha uma opção válida!")
                        except ValueError:
                                        print("escolha uma opção válida!")
                except ValueError:
                    print("escolha uma opção válida!")
        except Exception as e:
            print("Erro ao modificar usuário")
            print(f"Erro {e}")
    cursor.close()
    con.close()
                                    
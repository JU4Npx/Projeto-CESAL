from config.conexao import conexaoBD
from services.tools.name_CESAL import cesal_logo
import time
import os


def matricula():
        while True:
            con = conexaoBD()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM aluno ORDER BY ID_aluno")
            dados_alunos = cursor.fetchall()
            cesal_logo()
            print(f"-" * 30)
            print("        LISTA DE ALUNOS        ")
            print(f"-" * 30)
            print("")
            for dado in dados_alunos:
                print(f"ID: {dado[0]}  Nome: {dado[1]}  Idade: {dado[2]}  E-mail: {dado[3]}  Endereço: {dado[4]}  Telefone: {dado[5]}")
                print(f"-" * 120)
            try:
                print("")
                ID_aluno = (input("Digite o ID do aluno(a) que deseja editar, ou 0 para voltar: "))
                if ID_aluno == '0':
                    print("Voltando...")
                    time.sleep(1.5)
                    os.system('cls')
                    break
                else:
                    while True:
                        cursor.execute("SELECT * FROM aluno WHERE ID_aluno = %s", (ID_aluno,))
                        aluno = cursor.fetchone()
                        print(f"\nAluno selecionado: {aluno[1]} (ID {aluno[0]})")
                        print("Deseja continuar com a matrícula desse aluno?")
                        print("1 - Sim")
                        print("2 - Não")
                        opcao_aluno = input("\nDigite a opção desejada: ")
                        try:
                             if opcao_aluno == '1':
                                while True:
                                    cursor.execute("SELECT * FROM curso ORDER BY ID_curso")
                                    dados_curso = cursor.fetchall()
                                    print(f"-" * 30)
                                    print("        LISTA DE CURSOS        ")
                                    print(f"-" * 30)
                                    print("")
                                    for dado in dados_curso:
                                        print(f"ID: {dado[0]}  Nome: {dado[1]}  Descrição: {dado[2]}  Valor: {dado[3]}  Carga Horária: {dado[4]}  Vagas: {dado[5]}")
                                        print(f"-" * 120)
                                        print("")
                                    ID_curso = input("Digite o ID do curso que deseja matricular o aluno: ")
                                    try:
                                        if ID_curso is None:
                                            print("Curso não encontrado.")
                                            return
                                        else:
                                            cursor.execute("SELECT * FROM curso WHERE ID_curso = %s", (ID_curso,))
                                            curso = cursor.fetchone()
                                            if curso is None:
                                                print("Curso não encontrado.")
                                                return
                                            else:
                                                cursor.execute("SELECT ID_matricula FROM matricula WHERE ID_aluno = %s AND ID_curso = %s", (ID_aluno, ID_curso))
                                                matricula_existente = cursor.fetchone()
                                                if matricula_existente:
                                                                    print("O aluno já está matriculado neste curso.")
                                                                    input("Pressione Enter para continuar...")
                                                                    return
                                                print(f"\nCurso selecionado: {curso[1]} (ID {curso[0]})")
                                                print(f"Deseja confirmar a matrícula do aluno {aluno[1]}, no curso de {curso[1]}? ")
                                                print("1 - Sim")
                                                print("2 - Não")
                                                try:
                                                    opcao_curso = input("\nDigite a opção desejada: ")
                                                    if opcao_curso == '1':
                                                        try:
                                                            cursor.execute("SELECT numero_vagas FROM curso WHERE ID_curso = %s FOR UPDATE", (ID_curso,))
                                                            vagas_atuais = cursor.fetchone()[0]
                                                            if vagas_atuais <= 0:
                                                                print("Não há vagas disponíveis para este curso no momento.")
                                                                input("Pressione Enter para continuar...")
                                                                return
                                                            else:
                                                                cursor.execute("INSERT INTO matricula (ID_aluno, ID_curso) VALUES (%s, %s)", (ID_aluno, ID_curso))
                                                                cursor.execute("UPDATE curso SET numero_vagas = numero_vagas - 1 WHERE ID_curso = %s", (ID_curso,))
                                                                con.commit()
                                                                print("Matrícula realizada com sucesso!")
                                                                input("Pressione Enter para continuar...")
                                                                return
                                                        except Exception as e:
                                                            print(f"Erro ao realizar matrícula: {e}")
                                                            input("Pressione Enter para continuar...")
                                                            return
                                                    elif opcao_curso == '2':
                                                        print("Matrícula cancelada.")
                                                        break
                                                except ValueError:
                                                    print("Opção inválida. Tente novamente.")
                                                    continue
                                                break
                                    except Exception as e:
                                        print(f"Erro ao buscar curso")
                                        con.rollback()
                                        print(f"Erro: {e}")
                             else:
                                break
                        except ValueError:
                            print("Opção inválida. Tente novamente.")
                            continue
            except Exception as e:
                print(f"Erro ao buscar aluno")
                print(f"Erro: {e}")
            finally:
                cursor.close()
                con.close()

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


def lista_curso_disciplina():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("""SELECT
    c.nome_curso AS Curso,
    d.nome_disciplina AS Disciplina
FROM
    curso AS c
JOIN
    curso_disciplina AS cd ON c.ID_curso = cd.ID_curso
JOIN
    disciplina AS d ON cd.ID_disciplina = d.ID_disciplina
ORDER BY
    c.nome_curso, d.nome_disciplina;""")
    dados_curso_disciplina = cursor.fetchall()
    print(f"-" * 30)
    print("        LISTA DE CURSOS        ")
    print(f"-" * 30)
    print("")
    for dado in dados_curso_disciplina:
        print(f"Nome: {dado[0]}  Disciplina: {dado[1]}")
        print(f"-" * 120)
    input("Pressione ENTER para voltar ao menu...")
    cursor.close()
    con.close()                               

def lista_aluno_curso():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("""SELECT
    c.nome_curso AS Curso,
    a.nome_aluno AS Aluno,
    a.email_aluno AS Email_Aluno
FROM
    curso AS c
JOIN
    matricula AS m ON c.ID_curso = m.ID_curso
JOIN
    aluno AS a ON m.ID_aluno = a.ID_aluno
ORDER BY
    c.nome_curso, a.nome_aluno;""")
    dados_aluno_curso = cursor.fetchall()
    print(f"-" * 30)
    print("     LISTA DE ALUNOS POR CURSO        ")
    print(f"-" * 30)
    print("")
    for dado in dados_aluno_curso:
        print(f"Curso: {dado[0]}  Aluno: {dado[1]}  Email: {dado[2]}")
        print(f"-" * 120)
    input("Pressione ENTER para voltar ao menu...")
    cursor.close()
    con.close()


def lista_aluno_disciplina_curso():
    con = conexaoBD()
    cursor = con.cursor()
    cursor.execute("""SELECT
    C.nome_curso AS Curso,
    A.nome_aluno AS Aluno,
    D.nome_disciplina AS Disciplina
FROM
    curso AS C
INNER JOIN
    matricula AS M ON C.ID_curso = M.ID_curso
INNER JOIN
    aluno AS A ON M.ID_aluno = A.ID_aluno
INNER JOIN
    curso_disciplina AS CD ON C.ID_curso = CD.ID_curso
INNER JOIN
    disciplina AS D ON CD.ID_disciplina = D.ID_disciplina
ORDER BY
    C.nome_curso, A.nome_aluno, D.nome_disciplina;""")
    dados_aluno_disciplina_curso = cursor.fetchall()
    print(f"-" * 60)
    print("     LISTA DE ALUNOS E DISCIPLINAS POR CURSO        ")
    print(f"-" * 60)
    print("")
    for dado in dados_aluno_disciplina_curso:
        print(f"Curso: {dado[0]}  Aluno: {dado[1]}  Disciplina: {dado[2]}")
        print(f"-" * 120)
    input("Pressione ENTER para voltar ao menu...")
    cursor.close()
    con.close()

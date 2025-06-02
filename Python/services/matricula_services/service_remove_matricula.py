from config.conexao import conexaoBD

def remover_matricula():
        con = conexaoBD()
        cursor = con.cursor()
        cursor.execute("""SELECT
    m.ID_matricula AS ID_Matricula,
    a.nome_aluno AS Nome_Aluno,
    c.nome_curso AS Curso_Matriculado
FROM
    matricula AS m
JOIN
    aluno AS a ON m.ID_aluno = a.ID_aluno
JOIN
    curso AS c ON m.ID_curso = c.ID_curso
ORDER BY
    m.ID_matricula;""")
        dados_matriculas = cursor.fetchall()
        print(f"-" * 30)
        print("        LISTA DE MATRÍCULAS        ")
        print(f"-" * 30)
        print("")
        if not dados_matriculas:
            print("Nenhuma matrícula encontrada.")
            input("Pressione ENTER para voltar ao menu...")
            cursor.close()
            con.close()
            return
        for dado in dados_matriculas:
            print(f"ID de matricula: {dado[0]} | Aluno: {dado[1]} | Curso: {dado[2]}")
            print(f"-" * 120)
        while True:
            try:
                ID_matricula = input("Digite o ID da matrícula que deseja remover: ")
                cursor.execute("SELECT * FROM matricula WHERE ID_matricula = %s", (ID_matricula,))
                matricula = cursor.fetchone()
                if matricula is None:
                    print("Matrícula não encontrada.")
                    return  
                cursor.execute("DELETE FROM matricula WHERE ID_matricula = %s", (ID_matricula,))
                cursor.execute("UPDATE curso SET numero_vagas = numero_vagas + 1 WHERE ID_curso = %s", (matricula[2],))
                con.commit()
                print(f"Matrícula com ID {ID_matricula} removida com sucesso!")
                break   
            except Exception as e:
                print(f"Erro ao remover matrícula: {e}")
                con.rollback()
            finally:
                cursor.close()
                con.close()
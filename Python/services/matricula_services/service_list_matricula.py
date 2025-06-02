from config.conexao import conexaoBD

def listar_matricula():
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
    for dado in dados_matriculas:
        print(f"ID de matricula: {dado[0]} | Aluno: {dado[1]} | Curso: {dado[2]}")
        print("-" * 120)
    if not dados_matriculas:
        print("Nenhuma matrícula encontrada.")
    else:
        input("Pressione Enter para sair...")
    cursor.close()
    con.close()

from config.conexao import conexaoBD

def conexao_cadastro_curso(nome_curso, descricao, valor_curso, carga_horaria, numero_vagas):
    try:
        con = conexaoBD()
        cursor = con.cursor()
        query = "INSERT INTO curso (nome_curso, descricao, valor_curso, carga_horaria, numero_vagas) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nome_curso, descricao, valor_curso, carga_horaria, numero_vagas))
        con.commit()
        print("Curso Cadastrado com Sucesso!")
    except Exception as e:
        print("Erro ao cadastrar curso")
        print(f"Erro {e}")
    finally:
        cursor.close()
        con.close()

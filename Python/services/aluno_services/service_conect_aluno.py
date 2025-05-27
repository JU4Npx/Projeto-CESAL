from config.conexao import conexaoBD

def conexao_cadastro_aluno(nome_aluno, idade_aluno, email_aluno, endereco_aluno, telefone_aluno):
    try:
        con = conexaoBD()
        cursor = con.cursor()
        query = "INSERT INTO aluno (nome_aluno, idade_aluno, email_aluno, endereco_aluno, telefone_aluno) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nome_aluno, idade_aluno, email_aluno, endereco_aluno, telefone_aluno))
        con.commit()
        print("Aluno Cadastrado com Sucesso!")
    except Exception as e:
        print("Erro ao cadastrar aluno")
        print(f"Erro {e}")
    finally:
        cursor.close()
        con.close()
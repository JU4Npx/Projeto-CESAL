from config.conexao import conexaoBD

def conexao_cadastro_disciplina(nome_disciplina, descricao_disciplina):
    try:
        con = conexaoBD()
        cursor = con.cursor()
        query = "INSERT INTO disciplina (nome_disciplina, descricao_disciplina) VALUES (%s, %s)"
        cursor.execute(query, (nome_disciplina, descricao_disciplina))
        con.commit()
        print("Disciplina cadastrada com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar disciplina")
        print(f"Erro: {e}")
    finally:
        cursor.close()
        con.close()
    
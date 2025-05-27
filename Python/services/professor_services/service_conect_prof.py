from config.conexao import conexaoBD

def conexao_cadastro_professor(nome_professor, idade_professor, email_professor, telefone_professor, formacao):
    try:
        con = conexaoBD()
        cursor = con.cursor()
        query = "INSERT into professor (nome_professor, idade_professor, email_professor, telefone_professor, formacao) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nome_professor, idade_professor, email_professor, telefone_professor, formacao))
        con.commit()
        print("Professor cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar professor")
        print(f"Erro {e}")
    finally:
        cursor.close()
        con.close()
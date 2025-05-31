import base64
from config.conexao import conexaoBD
import bcrypt   


def conexao_cadastro_usuario(nome_usuario, email_usuario, senha_usuario, role):
    con = None
    cursor = None
    try:
        senha_bytes = senha_usuario.encode('utf-8')
        senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
        senha_hash_b64 = base64.b64encode(senha_hash).decode('utf-8')
        con = conexaoBD()
        cursor = con.cursor()
        query = ("INSERT INTO usuario (nome_usuario, email_usuario, senha_hash, role) VALUES (%s, %s, %s, %s)")
        cursor.execute(query, (nome_usuario, email_usuario, senha_hash_b64, role))
        con.commit()
        print("Usuário registrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar usuário")
        print(f"Erro: {e}")
    finally:
        cursor.close()
        con.close()
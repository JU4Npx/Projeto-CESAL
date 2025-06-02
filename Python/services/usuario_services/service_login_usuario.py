import bcrypt
import base64
from config.conexao import conexaoBD
import pwinput

def fazer_login_usuario(): 
    try:
        con = conexaoBD()
        cursor = con.cursor()
        email = input("Digite seu email: ")
        cursor.execute("SELECT senha_hash, role, nome_usuario FROM usuario WHERE email_usuario = %s", (email,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("Usuário não encontrado.")
            return None, None

        senha_hash_base64, role, nome_usuario = resultado
        senha_digitada = pwinput.pwinput(prompt ="Digite sua senha: ", mask='*')
        senha_bytes = senha_digitada.encode('utf-8')
        senha_hash = base64.b64decode(senha_hash_base64)

        if bcrypt.checkpw(senha_bytes, senha_hash):
            print("Login realizado com sucesso!")
            return role, nome_usuario
        else:
            print("Senha incorreta.")
            return None,None

    except Exception as e:
        print(f"Erro ao fazer login: {e}")
        return None, None
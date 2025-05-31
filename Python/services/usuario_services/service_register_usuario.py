from services.tools.tools import validacao_email
from services.usuario_services.service_conect_usuario import conexao_cadastro_usuario
import pwinput


def cadastro_usuario():
    nome_usuario = input("Por favor, digite o nome do usuário: ")
    while True:
        email_usuario = input("Por favor, digite o e-mail do usuário: ")
        if not validacao_email(email_usuario):
            print("Email inválido, tente novamente.")
        else:
            break
    while True:
        try:
         senha_usuario = pwinput.pwinput(prompt ="Por favor, digite a senha do usuário (mínimo 8 caractéres): ", mask='*')
         if len(senha_usuario) < 8:
            print("A senha precisar ter no mínimo 8 caracteres!")
         else:
            break
        except Exception as e:
            print("Erro ao cadastrar a senha!")
            print(f"Erro {e}")
    while True:
        print("Esse usuário será administrador? ")
        print("")
        print("1 - sim")
        print("2 - Não")
        opcao = input("\nOpção: ")

        match opcao:
            case "1":
                role = "admin"
                break
            case "2":
                role = "user"
                break
            case _:
                print("Opção inválida. Tente novamente.")
    conexao_cadastro_usuario(nome_usuario, email_usuario, senha_usuario, role)



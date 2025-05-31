from services.aluno_services.service_conect_aluno import conexao_cadastro_aluno
from services.tools.tools import validacao_email

def cadastro_aluno():
    nome_aluno     = input("Por favor, digite o nome do aluno: ")
    while True:
        idade_aluno    = input("Por favor, digite a idade do aluno: ")
        try:
            idade = int(idade_aluno)
            if idade <= 15:
                print("Idade inválida, o aluno não pode ter menos que dezesseis anos.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    while True:
        email_aluno = input("Por favor, digite o e-mail do aluno: ")
        if not validacao_email(email_aluno):
            print("Email inválido, tente novamente.")
        else:
            break
    endereco_aluno = input("Por favor, digite o endereço do aluno: ")
    while True:
        telefone_aluno = input("Por favor, digite o telefone do aluno(com '55' + DDD e os números sem espaço): ")
        if len(telefone_aluno) < 12:
            print("Telefone inválido. Deve conter pelo menos 12 dígitos.")
        elif not telefone_aluno.isdigit():
            print("Telefone inválido. Use apenas números.")
        else:
            break
    conexao_cadastro_aluno(nome_aluno, idade, email_aluno, endereco_aluno, telefone_aluno)
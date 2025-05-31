from services.tools.tools import validacao_email
from services.professor_services.service_conect_prof import conexao_cadastro_professor

def cadastro_professor():
    nome_professor   = input("Por favor, digite o nome do professor: ")
    while True:
        idade_professor   = input("Por favor, digite a idade do professor: ")
        try:
            idade = int(idade_professor)
            if idade <= 18:
                print("Idade inválida, o professor não pode ter menos que dezoito anos.")
            #A idade minima é 18 pois podem ser cadastrados também monitores/estagiários.
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    while True:
        email_professor   = input("Por favor, digite o e-mail do professor: ")
        if not validacao_email(email_professor):
            print("Email inválido, tente novamente.")
        else:
            break
    while True:
        telefone_professor = input("Por favor, digite o telefone do professor (com '55' + DDD e os números sem espaço): ")
        if len(telefone_professor) != 13:
            print("Telefone inválido.")
        elif not telefone_professor.isdigit():
            print("Telefone inválido. Use apenas números.")
        else:
            break
    formacao         = input("Por favor, informe a formação acadêmica do professor: ")
    conexao_cadastro_professor(nome_professor, idade, email_professor, telefone_professor, formacao)
    

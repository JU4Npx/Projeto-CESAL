from services.curso_services.service_conect_cursos import conexao_cadastro_curso

def cadastro_curso():
    nome_curso       = input("Por favor, digite o nome do curso: ")
    descricao        = str(input("Por favor, escreva uma breve descrição do curso: "))
    while True:
        valor_curso      = input("Por favor, informe o valor do curso: ")
        try:
            valor = float(valor_curso)
            if valor <= 0:
                print("Número inválido, o valor não pode ser menor ou igual a zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    while True:
        carga_horaria    = input("Por favor, informe a carga horária em horas: ")
        try:
            carga = int(carga_horaria)
            if carga <= 0:
                print("Valor inválido, a carga horária não pode ser menor, ou igual a zero")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    while True:
        numero_vagas     = input("Por favor, informe o número de vagas disponíveis: ")
        try:
            vagas = int(numero_vagas)
            if vagas < 0:
                print("Valor inválido, o número de vagas não pode ser menor que zero")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    conexao_cadastro_curso(nome_curso, descricao, valor, carga, vagas)

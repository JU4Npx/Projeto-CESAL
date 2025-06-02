from services.disciplina_Services.service_conect_disciplina import conexao_cadastro_disciplina

def cadastrar_disciplina():
    while True:
        nome_disciplina = input("Digite o nome da disciplina: ")
        descricao_disciplina = input("Digite a descrição da disciplina: ")
        conexao_cadastro_disciplina(nome_disciplina, descricao_disciplina)
        input("Pressione Enter para continuar...")
        break
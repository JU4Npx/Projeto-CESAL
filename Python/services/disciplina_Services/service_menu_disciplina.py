from services.disciplina_Services.service_register_disciplina import cadastrar_disciplina
from services.disciplina_Services.service_list_disciplina import lista_disciplina
from services.tools.name_CESAL import cesal_logo
import os


def menu_disciplina():
    while True:
        os.system('cls')
        cesal_logo()
        print(f"-" * 30)
        print("       DISCIPLINA        ")
        print(f"-" * 30)
        print("\n1 - Cadastrar Disciplina")
        print("\n2 - Listar Disciplinas")
        print("\n0 - Voltar ao Menu Principal")
        
        opcao = input("\nDigite a opção desejada: ")
        try:
            if opcao == '1':
                cadastrar_disciplina()
            elif opcao == '2':
                lista_disciplina()
            elif opcao == '0':
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida, por favor digite um número.")
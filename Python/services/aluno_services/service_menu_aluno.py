import os
import time
from services.tools.name_CESAL import cesal_logo
from services.aluno_services.service_register_aluno import cadastro_aluno
from services.aluno_services.service_list_aluno import lista_aluno, editar_lista_aluno
from services.aluno_services.service_remove_aluno import remover_aluno


def menu_aluno():
    while True:
        os.system('cls')
        cesal_logo()
        print(f"-" * 30)
        print("         MENU ALUNO       ")
        print(f"-" * 30)
        print("\n1 - Cadastrar Aluno")
        print("\n2 - Lista de Alunos")
        print("\n3 - Editar Aluno")
        print("\n4 - Remover Aluno")
        print("\n0 - Voltar ao Menu Principal")
        
        try:
            opcao = int(input("\nDigite a opção desejada: "))
            if opcao == 1:
                cadastro_aluno()
            elif opcao == 2:
                lista_aluno()
            elif opcao == 3:
                editar_lista_aluno()
            elif opcao == 4:
                remover_aluno()
            elif opcao == 0:
                break
            else:
                print("Opção inválida, tente novamente.")
            time.sleep(2)
        except ValueError:
            print("Entrada inválida, por favor digite um número.")
            time.sleep(2)
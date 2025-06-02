import os
import time
from services.tools.name_CESAL import cesal_logo
from services.professor_services.service_register_prof import cadastro_professor
from services.professor_services.service_list_prof import lista_professor, editar_lista_professor
from services.professor_services.service_remove_prof import remover_professor


def menu_professor():
    while True:
        os.system('cls')
        cesal_logo()
        print(f"-" * 30)
        print("         MENU PROFESSOR       ")
        print(f"-" * 30)
        print("\n1 - Cadastrar Professor")
        print("\n2 - Lista de Professores")
        print("\n3 - Editar Professor")
        print("\n4 - Remover Professor")
        print("\n0 - Voltar ao Menu Principal")
        try:
            opcao = int(input("\nDigite a opção desejada: "))
            if opcao == 1:
                cadastro_professor()
            elif opcao == 2:
                lista_professor()
            elif opcao == 3:
                editar_lista_professor()
            elif opcao == 4:
                remover_professor()
            elif opcao == 0:
                break
            else:
                print("Opção inválida, tente novamente.")
            time.sleep(2)
        except ValueError:
            print("Entrada inválida, por favor digite um número.")
            time.sleep(2)
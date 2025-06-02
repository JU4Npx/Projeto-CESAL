from services.matricula_services.service_register_matricula import matricula
from services.matricula_services.service_list_matricula import listar_matricula
from services.matricula_services.service_remove_matricula import remover_matricula
from services.tools.name_CESAL import cesal_logo
import os


def menu_matricula():
    while True:
        os.system('cls')
        cesal_logo()
        print(f"-" * 30)
        print("       MATRÍCULA        ")
        print(f"-" * 30)
        print("\n1 - Realizar Matrícula")
        print("\n2 - Lista de Matrículas")
        print("\n3 - Remover Matrícula")
        print("\n0 - Voltar ao Menu Principal")
        
        opcao = input("\nDigite a opção desejada: ")
        try:
            if opcao == '1':
                matricula()
            elif opcao == '2':
                listar_matricula()
            elif opcao == '3':
                remover_matricula()
            elif opcao == '0':
                print("Voltando ao menu principal...")
                break
        except ValueError:
            print("Entrada inválida, por favor digite um número.")

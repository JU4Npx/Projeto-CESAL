import os
import time
from services.tools.name_CESAL import cesal_logo
from services.curso_services.service_register_cursos import cadastro_curso
from services.curso_services.service_list_cursos import lista_curso, editar_lista_curso
from services.curso_services.service_remove_curso import remover_curso


def menu_curso():
    while True:
        os.system('cls')
        cesal_logo()
        print(f"-" * 30)
        print("         MENU CURSO       ")
        print(f"-" * 30)
        print("")
        print("1 - Cadastrar Curso")
        print("2 - Lista de Cursos")
        print("3 - Editar Curso")
        print("4 - Remover Curso")
        print("0 - Voltar ao Menu Principal")
        print("")
        
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                cadastro_curso()
            elif opcao == 2:
                lista_curso()
            elif opcao == 3:
                editar_lista_curso()
            elif opcao == 4:
                remover_curso()
            elif opcao == 0:
                break
            else:
                print("Opção inválida, tente novamente.")
            time.sleep(2)
        except ValueError:
            print("Entrada inválida, por favor digite um número.")
            time.sleep(2)
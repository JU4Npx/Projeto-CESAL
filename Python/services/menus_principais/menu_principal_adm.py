import os
import time
from services.tools.name_CESAL import cesal_logo
from services.aluno_services.service_menu_aluno import menu_aluno
from services.professor_services.service_menu_prof import menu_professor
from services.curso_services.service_menu_curso import menu_curso
from services.usuario_services.service_menu_usuario import menu_usuario

def menu_principal_adm():
    while True:
        os.system('cls')
        cesal_logo()
        print(f"-" * 30)
        print("      MENU ADMINISTRADOR       ")
        print(f"-" * 30)
        print("")
        print("\n1 - Central Aluno")
        print("\n2 - Central Professor")
        print("\n3 - Central Curso")
        print("\n4 - Central Usuário")
        print("\n0 - Sair")
        print("")
        
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                menu_aluno()
            elif opcao == 2:
                menu_professor()
            elif opcao == 3:
                menu_curso()
            elif opcao == 4:
                menu_usuario()
            elif opcao == 0:
                print("Saindo do sistema...")
                time.sleep(2)
                break
            else:
                print("Opção inválida, tente novamente.")
            time.sleep(2)
        except ValueError:
            print("Entrada inválida, por favor digite um número.")
            time.sleep(2)
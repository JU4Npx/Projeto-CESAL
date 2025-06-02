import os
import time
from services.tools.name_CESAL import cesal_logo
from services.usuario_services.service_conect_usuario import conexao_cadastro_usuario
from services.usuario_services.service_register_usuario import cadastro_usuario
from services.usuario_services.service_list_usuario import lista_usuario, editar_lista_usuario
from services.usuario_services.service_remove_usuario import remover_usuario

def menu_usuario():
    while True:
        os.system('cls')
        cesal_logo()
        print(f"-" * 30)
        print("         MENU USUÁRIO       ")
        print(f"-" * 30)
        print("\n1 - Cadastrar Usuário")
        print("\n2 - Lista de Usuários")
        print("\n3 - Editar Usuário")
        print("\n4 - Remover Usuário")
        print("\n0 - Voltar ao Menu Principal")
        
        try:
            opcao = int(input("\nDigite a opção desejada: "))
            if opcao == 1:
                cadastro_usuario()
            elif opcao == 2:
                lista_usuario()
            elif opcao == 3:
                editar_lista_usuario()
            elif opcao == 4:
                remover_usuario()
            elif opcao == 0:
                break
            else:
                print("Opção inválida, tente novamente.")
            time.sleep(2)
        except ValueError:
            print("Entrada inválida, por favor digite um número.")
            time.sleep(2)
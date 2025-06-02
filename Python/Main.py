import os
from services.tools.name_CESAL import cesal_logo
from services.usuario_services.service_login_usuario import fazer_login_usuario
from services.menus_principais.menu_principal_adm import menu_principal_adm
from services.menus_principais.menu_principal_usuario import menu_principal_usuario

def menu_principal():
    while True:
        cesal_logo()
        role, nome_usuario = fazer_login_usuario()
        if role is None:
            print("Falha no login. Encerrando o programa.")
            return
        elif role == 'admin':
            print(f"Bem-vindo, {nome_usuario}! Você tem acesso ao menu de administração.")
            input("Pressione Enter para continuar...")
            menu_principal_adm()      
        else:
            print(f"Bem-vindo, {nome_usuario}! Você tem acesso ao menu de usuário.")
            input("Pressione Enter para continuar...")
            menu_principal_usuario()
        os.system('cls')

menu_principal()